# Library for 7Zip and OS reach
# Main code.
import py7zr
import os
import pandas as pd
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()

from scripts import listofteams, country

from pymongo import MongoClient

atlas_uri = os.environ.get("ATLAS_URI")

# Connection to MongoDB
client = MongoClient(atlas_uri)
fifam = client["fifam"]
stadiums = fifam["stadiums"]

# Returns today
def date(targetpath):
    date = datetime.today().strftime('%Y-%m-%d')
    print(f"Creating folder for {date}")
    # If the date folder does not exists then it creates
    if os.path.exists(f'{targetpath}/{date}') == False:
        os.mkdir(f"{targetpath}/{date}")
    return date

# Checks if stadium is previously packed
def checker(v):
    list = []
    for path in Path().rglob(f'*{v}*.7z'):
        path = str(path)
        list.append(path)
    if len(list) > 0:
        return True
    else:
        return False

def writer(archive,v):
    archive.writeall(f"{pathnew}/{v}", f"data/stadium/FIFA/{v}")

# Used for packing a folder with a parent folder. mode r is for read. w is for write
def pack(pathnew,d,de,date,targetpath):
    for k, v in d.items():
    # Now, if the complete.txt is included in the folder, then it will be packed.
            if os.path.isfile(f'{pathnew}/{v}/complete.txt') == True:
                # It will also check if the file is already written.
                if v[4:] == "FFFF":
                    if checker(v) == False:
                    # Creates extra folder for national teams
                        if os.path.exists(f'{targetpath}/{date}/National Teams') == False:
                            os.mkdir(f"{targetpath}/{date}/National Teams")
                            print(f"Writing archive for {k}...")
                        with py7zr.SevenZipFile(f'{targetpath}/{date}/National Teams/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v)  
                        d = {"teamName": k, "teamId": f"0x{v}", "country": "National Teams", "date": date, "file": f'{v} - {k}.7z'}
                        insert_d = stadiums.insert_one(d)
                    else:
                        continue
                elif os.path.exists(f'{targetpath}/{date}/{de.get(v[2:4])}') == False:
                    if checker(v) == False:
                        os.mkdir(f"{targetpath}/{date}/{de.get(v[2:4])}")
                        print(f"Writing archive for {k}...")
                        with py7zr.SevenZipFile(f'{targetpath}/{date}/{de.get(v[2:4])}/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v)
                        d = {"teamName": k, "teamId": f"0x{v}", "country": f"{de.get(v[2:4])}", "date": date, "file": f'{v} - {k}.7z'}
                        insert_d = stadiums.insert_one(d)     
                else:
                    # Eğer paket yapılmadıysa yapsın
                    if checker(v) == False:
                        print(f"Writing archive for {k}...")
                        with py7zr.SevenZipFile(f'{targetpath}/{date}/{de.get(v[2:4])}/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v) 
                        # adds stadium to MongoDB database.
                        d = {"teamName": k, "teamId": f"0x{v}", "country": f"{de.get(v[2:4])}", "date": date, "file": f'{v} - {k}.7z'}
                        insert_d = stadiums.insert_one(d)

# Main function.
if __name__ == "__main__":
# Game folder
    pathbase="D:\Games\FIFA Manager 14"
    pathnew=pathbase+"\data\stadium\FIFA"
    teamlist = listofteams.listofteams()
    coun = country.country()
    targetpath = "FM Stadiums"
    date = "2025-01-12"
    # list = retrievelist(pathnew)
    export = pack(pathnew,teamlist,coun,date,targetpath)