# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from collections import Counter

matches = pd.read_json('data/matches.json')

teams = []

wins = []

# matches.tail()

# matches.info()

# matches.describe()

i = 2

for i in range(2,50):
    # team_a = matches["results"][i][0]["team_id"]
    # match_result = matches["results"][i][0]["score"]
    
    # print("Team {} had a result of: {}".format(team_a,match_result))
    # print(len(teams))

########## This is not working, trying to populate an empty array. ################

    wins.append(matches["winner"][i]["acronym"])

    if(matches["winner"][i]["acronym"] in teams):
        # print("Repeating at: {}".format(j))
        i += 1
    else:
        teams.append(matches["winner"][i]["acronym"])

        

###################################################################################
print(wins)

a = dict(Counter(wins))

print(a)

windf = pd.DataFrame(data=wins,columns=['List'])

windf.List.hist()

# plt.bar([row[0] for row in wins], [row[0] for row in wins])

    # ploting_winners =  matches["winner"][i]["acronym"]

    # print(matches["winner"][i]["acronym"] , "time in loop: {}".format(i))

# matches["winner"][4]["acronym"]



# %%



