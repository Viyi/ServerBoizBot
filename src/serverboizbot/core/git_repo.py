import git
import os
import logging
from pydantic import BaseModel
from collections import Counter

logger = logging.getLogger(__name__)

ALIASES = {"Viyi": "Arthur H"}


class GitInformation(BaseModel):
    current_sha: str
    branch: str
    commit_message: str
    author: str
    shortlog_stats: str
    total_commits: int
    total_files: int

    @property
    def merged_user_commits_table(self):
        lines = self.shortlog_stats.strip().split("\n")
        new_stats = Counter()
        for line in lines:
            count, author = line.strip().split(None, 1)
            if alias := ALIASES.get(author):
                new_stats[alias] += int(count)
            else:
                new_stats[author] += int(count)

        output = "```\n"
        output += f"{'Author':<20} | {'Commits'}\n"
        output += "-" * 30 + "\n"
        for author, count in new_stats.items():
            label = "commit" if count == 1 else "commits"
            output += f"{author:<20} | {count} {label}\n"

        output += "```"
        return output

    def __str__(self):
        lines = [
            "## 📊 Git Repository Stats",
            f"**{'Total Commits:':<17}** `{self.total_commits}`",
            f"**{'Total Files:':<23}** `{self.total_files}`",
            "### 📝 Latest Commit",
            f"`{self.commit_message.strip()}`",
            "",
            f"**Author:** `{self.author}`",
            f"**Branch:** `{self.branch}`",
            f"**SHA:** `{self.current_sha}`",
            "",
            "### 📈 Contributor Statistics",
            f"{self.merged_user_commits_table}",
        ]
        return "\n".join(lines)


def git_info() -> GitInformation | None:
    try:
        repo = git.Repo(os.getcwd(), search_parent_directories=True)

        total_commits = repo.git.rev_list("--count", "--all")

        files = repo.git.ls_files().split("\n")
        total_files = len([f for f in files if f])

        shortlog_stats = repo.git.shortlog("-sn", "--all")

        return GitInformation(
            current_sha=repo.head.object.hexsha,
            branch=repo.active_branch.name,
            commit_message=repo.head.commit.message,
            author=repo.head.commit.author.name,
            shortlog_stats=shortlog_stats,
            total_commits=total_commits,
            total_files=total_files,
        )
    except git.InvalidGitRepositoryError:
        logger.error("This directory is not a Git repository.")
        return None
