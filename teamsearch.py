import pandas as pd

# DeMeppfines dataframe
df = pd.read_excel('TeamsMini.xlsx')

# Defines dictionary. It sets new index as team. Then takes the transpose of dataframe, converts the dataframe to dictionary. Then we have a list output, we strip it from list.
d = (df.set_index('Team').T.to_dict('records')[0])

def searchfunc(d, name):
    for k,v in d.items():
        if k.__contains__(name):
            # prints key and value
            print(v+" - "+k)          

if __name__ == "__main__":
    name = input("search?")
    result = searchfunc(d, name)