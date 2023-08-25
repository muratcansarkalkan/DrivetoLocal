import json
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the parent directory (project directory)
project_dir = os.path.dirname(current_dir)

# Construct the full path to the JSON file in the data directory
json_file_path = os.path.join(project_dir, "staticdata", "teamsMini.json")

# Conversion of team database to a dictionary.
def listofteams():
    data = json.loads(open(json_file_path).read())
    print("Reading team list...")
    data_new = {item['Team']:item['UID'] for item in data}
    return data_new