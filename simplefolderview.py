import os

# Used for retrieving the available stadiums.
def retrievelist(path):
    # We used scandir instead of listdir. os.listdir(path) gives str. os.scandir(path) gave iterator instead
    # Burada eğer os.scandir(path) sonucu, is_dir ise yani bir klasörse, klasörün adını (f.name) verecek.
    return [f.name for f in os.scandir(path+"\data\stadium\FIFA") if f.is_dir()]
    # This line is same with these 3 lines. But these 3 lines give only 1 output while I want whole.
    # for f in os.scandir(path):
    #     if f.is_dir() == True:
    #         return f.name

# Just input parent folder.
path=input("Specify the folder that you installed the game")
retrievelist(path)
