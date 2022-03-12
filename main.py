# Library for 7Zip and OS reach
# Main code.
import py7zr
import os
import pandas as pd
from datetime import datetime
from pathlib import Path

# Conversion of team database to a dictionary.
def listofteams():
    df = pd.read_excel('TeamsMini.xlsx')
    d = (df.set_index('Team').T.to_dict('records')[0])
    return d

# Conversion of country database to a dictionary.
def country():
    dg = pd.read_excel('countriesnew.xlsx')
    de = (dg.set_index('Country').T.to_dict('records')[0])
    return de

# Returns today
def date():
    date = datetime.today().strftime('%Y-%m-%d')
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
                        os.mkdir(f"FM Stadiums/{date}/National Teams")
                        with py7zr.SevenZipFile(f'FM Stadiums/{date}/National Teams/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v)  
                    else:
                        continue
                elif os.path.exists(f'FM Stadiums/{date}/{de.get(v[2:4])}') == False:
                    if checker(v) == False:
                        os.mkdir(f"FM Stadiums/{date}/{de.get(v[2:4])}")
                        with py7zr.SevenZipFile(f'FM Stadiums/{date}/{de.get(v[2:4])}/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v)            
                else:
                    # Eğer paket yapılmadıysa yapsın
                    if checker(v) == False:
                        with py7zr.SevenZipFile(f'FM Stadiums/{date}/{de.get(v[2:4])}/{v} - {k}.7z', mode = "w") as archive:
                            writer(archive,v) 

# Main function.
if __name__ == "__main__":
    pathbase=input("Specify the folder that you installed the game")
    pathnew=pathbase+"\data\stadium\FIFA"
    teamlist = listofteams()
    coun = country()
    date = date()
    # list = retrievelist(pathnew)
    export = pack(pathnew,teamlist,coun,date)