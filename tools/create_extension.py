from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import pyrootutils


def take_multi_input(prompt):
    temp_list = []
    prompt = prompt + " Enter q to skip. "
    temp_input = input(prompt)
    
    while temp_input.lower() != "q":
        temp_list.append(temp_input)
        temp_input = input(prompt)
        
    return temp_list
    

# The part where we gather inputs

extension_name = input("Enter your new extension's name. eg. Calendar, RedditScraper: ")
file_name = input("Enter your desired filename. eg. calendar, reddit_scraper: ")

commands = take_multi_input("Enter your desired bot commands. (One at a time)")

listener_example = False if input("Include listener example? (Y/n) ").lower() == "n" else True


# The part where we write the template
root_path = pyrootutils.find_root()

env = Environment(loader=FileSystemLoader(root_path / "tools"))
template = env.get_template('extension.py.j2')

data = {"extension_name": extension_name, "commands": commands, "listener_example": listener_example}

output = template.render(data)

file_path = root_path / "src/serverboizbot/bot/extensions" / Path(file_name).with_suffix(".py")
with open(file_path, "w") as f:
    f.write(output)

print("New extension has been written to", file_path)



