import git
import os
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class GitInformation(BaseModel):
    current_sha: str
    branch: str
    commit_message: str
    author: str
    
    def __str__(self):
        return f"Git Info:\n  {self.commit_message.strip()}\n  Author: {self.author}\n  Branch: {self.branch}:{self.current_sha}"
    
    
def git_info() -> GitInformation | None:
    try:
        repo = git.Repo(os.getcwd(), search_parent_directories=True)
        
        return GitInformation(current_sha=repo.head.object.hexsha, branch=repo.active_branch.name, commit_message=repo.head.commit.message, author=repo.head.commit.author.name)
    except git.InvalidGitRepositoryError:
        logger.error("This directory is not a Git repository.")
        return None
        
