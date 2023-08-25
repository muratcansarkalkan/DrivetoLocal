# Library for 7Zip and OS reach
# Main code.
import py7zr
import os
import pandas as pd
from datetime import datetime
from pathlib import Path
import json

from pymongo import MongoClient

# Connection to MongoDB
client = MongoClient('mongodb+srv://muratcansarkalkan:muratcansarkalkan@cluster0.mcr0yu5.mongodb.net/fifam')
fifam = client["fifam"]
stadiums = fifam["stadiums"]

# Conversion of team database to a dictionary.
def listofteams():
    teams = "teamsMini.json"
    data = json.loads(open(teams).read())
    print("Reading team list...")
    data_new = {item['Team']:item['UID'] for item in data}
    return data_new

# Conversion of country database to a dictionary.
def country():
    coun = "countriesnew.json"
    data = json.loads(open(coun).read())
    print("Reading country data...")
    data_new = {item['Country']:item['Name'] for item in data}
    return data_new

# You need a directory as FM Stadiums. Sync this from GoogleDrive

# Returns today
def date():
    date = datetime.today().strftime('%Y-%m-%d')
    print(f"Creating folder for {date}")
    # If the date folder does not exists then it creates
    if os.path.exists(f'FM Stadiums/{date}') == False:
        os.mkdir(f"FM Stadiums/{date}")

    return date
# Used for retrieving the available stadiums. This applies to end user. not me
# def retrievelist(pathnew):
#     # We used scandir instead of listdir. os.listdir(path) gives str. os.scandir(path) gave list of folders instead
#     # If scanned paths are a directory then the name will be given.
#     list = ([f.name for f in os.scandir(pathnew) if f.is_dir()])
#     return list

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
def pack(pathnew,d,de,date):
    for k, v in d.items():
    # Now, if the complete.txt is included in the folder, then it will be packed.
            if os.path.isfile(f'{pathnew}/{v}/complete.txt') == True:
                # It will also check if the file is already written.
                if v[4:] == "FFFF":
                    if checker(v) == False:
                    # Creates extra folder for national teams
                        if os.path.exists(f'FM Stadiums/{date}/National Teams') == False:
                            os.mkdir(f"FM Stadiums/{date}/National Teams")
                            print(f"Writing archive for {k}...")
                        with py7zr.SevenZipFile(f'FM Stadiums/{date}/National Teams/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v)  
                        d = {"teamName": k, "teamId": v, "country": "National Teams", "date": date, "file": f'{v} - {k}.7z'}
                        insert_d = stadiums.insert_one(d)
                    else:
                        continue
                elif os.path.exists(f'FM Stadiums/{date}/{de.get(v[2:4])}') == False:
                    if checker(v) == False:
                        os.mkdir(f"FM Stadiums/{date}/{de.get(v[2:4])}")
                        print(f"Writing archive for {k}...")
                        with py7zr.SevenZipFile(f'FM Stadiums/{date}/{de.get(v[2:4])}/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v)   
                        d = {"teamName": k, "teamId": v, "country": f"{de.get(v[2:4])}", "date": date, "file": f'{v} - {k}.7z'}
                        insert_d = stadiums.insert_one(d)     
                else:
                    # Eğer paket yapılmadıysa yapsın
                    if checker(v) == False:
                        print(f"Writing archive for {k}...")
                        with py7zr.SevenZipFile(f'FM Stadiums/{date}/{de.get(v[2:4])}/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v) 
                        # adds stadium to MongoDB database.
                        d = {"teamName": k, "teamId": f"0x{v}", "country": f"{de.get(v[2:4])}", "date": date, "file": f'{v} - {k}.7z'}
                        insert_d = stadiums.insert_one(d)

# teamName, teamId, country, date, file
# teamName: k
# teamId: v
# country: {de.get(v[2:4])} OR National Teams
# date: date
# file: {v} - {k}.7z

# Main function.
if __name__ == "__main__":
# Game folder
    pathbase="D:\Games\FIFA Manager 14"
    pathnew=pathbase+"\data\stadium\FIFA"
    teamlist = listofteams()
    coun = country()
    date = date()
    # list = retrievelist(pathnew)
    export = pack(pathnew,teamlist,coun,date)