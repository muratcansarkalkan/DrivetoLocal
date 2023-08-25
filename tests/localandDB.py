import glob, os
import unittest
from dotenv import load_dotenv
# Load variables from .env file

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the parent directory
parent_dir = os.path.dirname(current_dir)

# Construct the path to the .env file in the parent directory
env_file_path = os.path.join(parent_dir, '.env')
fm_stadia_path = os.path.join(parent_dir, 'FM Stadiums')

# Load variables from the .env file
load_dotenv(dotenv_path=env_file_path)

atlas_uri = os.environ.get("ATLAS_URI")

from pymongo import MongoClient

client = MongoClient(atlas_uri)
fifam = client["fifam"]
stadiums = fifam["stadiums"]

getStadia = stadiums.find({})
mongoStadia = []
# Obtains .7z files included in MongoDB database
for document in getStadia:
    x_value = document.get('file')
    if x_value is not None:
        mongoStadia.append(x_value)

localStadia = []
# Obtains .7z files included in local path
exclude = ['Others']
for root, dirs, files in os.walk(fm_stadia_path):
    [dirs.remove(d) for d in list(dirs) if d in exclude]
    for file in files:
        if file.endswith(".7z"):
            localStadia.append(file)

elements_not_in_local = [element for element in mongoStadia if element not in localStadia]
elements_not_in_mongo = [element for element in localStadia if element not in mongoStadia]

class TestStringMethods(unittest.TestCase):
    def test_checkfiletotal(self):
        self.assertEqual(len(localStadia), len(mongoStadia), (f'Missing in local drive: {elements_not_in_local}, Missing in MongoDB collection: {elements_not_in_mongo}'))

if __name__ == '__main__':
    unittest.main()
