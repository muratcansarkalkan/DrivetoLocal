import json
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the parent directory (project directory)
project_dir = os.path.dirname(current_dir)

# Construct the full path to the JSON file in the data directory
json_file_path = os.path.join(project_dir, "staticdata", "countriesnew.json")

# Conversion of country database to a dictionary.
def country():
    data = json.loads(open(json_file_path).read())
    print("Reading country data...")
    data_new = {item['Country']:item['Name'] for item in data}
    return data_new