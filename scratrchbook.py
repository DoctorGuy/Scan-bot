##Fantsy data
import pandas as pd
import numpy as np
import plotly as p
import seaborn as sns
import matplotlib as mp
import csv
import os

os.chdir('C:/Users/ellio/Documents/Projects/Fantasy_scoring')
defense = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_DST.csv")
Kik = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_K.csv")
QB = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_QB.csv")
RB = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_RB.csv")
TE = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_TE.csv")
WR = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_WR.csv")

##Questions to answer
##1##
##How could I have drafted better?
##Rules: I know what I know now, I can use avg ppg to select a better posityion at my pick. If I take someone elses pick, we essentially trade, and they take who I took in that round. 
##So if I got saquon barkely in the first, then someone else would get my first round pick of cooper kupp. 
#3We are trying 3 strategies:
##take the most points, no matter what...
## ROBUST: RB/RB/WR/WR/RB/QB/RB/TE/RB/WR/WR/QB/WR/RB/DST/K
## Kelce: TE/RB/WR/WR/RB/QB/RB/RB/WR/RB/WR/QB/WR/RB/K/DST. 

df = pd.read_csv('draft.csv')
df[['Name', 'Position']] = df['PLAYER'].str.split(',', n=1, expand=True)
df = df.drop(columns=['PLAYER'])    
df = df[['Number', 'Position', 'TEAM', 'Name']]
df['Name'] = df['Name'].apply(lambda x: " ".join(x.split()[:2]))
df['Position'] = df['Position'].apply(lambda x: str(x).replace(u'\xa0', u''))




def1 = defense[['Player', 'FPTS/G']]
kik1 = Kik[['Player', 'FPTS/G']]
QB1 = QB[['Player', 'FPTS/G']]
RB1 = RB[['Player', 'FPTS/G']]
TE1 = TE[['Player', 'FPTS/G']]
WR1 = WR[['Player', 'FPTS/G']]

one = pd.concat([def1,kik1,QB1,RB1,TE1,WR1],ignore_index= True)
one['Player'] = one['Player'].str.replace('(\(.*\))', '')
one['Player'] = one['Player'].str.strip()
df['Name'] = df['Name'].str.strip()
points = df.merge(one, left_on= 'Name', right_on= 'Player', how='left')
sorted_df = points.sort_values('Number')
del sorted_df['Name']
sorted_df['Round'] = [i//10+1 for i in range(len(sorted_df))]
sorted_df['Used'] = 0

key_diff = set(one.Player).difference(sorted_df.Player)
where_diff = one.Player.isin(key_diff)

# Slice TableB accordingly and append to TableA
sorted_df = sorted_df.append(one[where_diff], ignore_index=True)
sorted_df['Number'] = range(1, len(sorted_df) + 1)



df = sorted_df

##Manually attr positions
df['Position'] = np.where(df['Player'] == 'Patriots D/ST', 'D/ST', df['Position'])
df['Position'] = np.where(df['Player'] == 'Geno Smith', 'QB', df['Position'])
df['Position'] = np.where(df['Player'] == 'Jerick McKinnon', 'RB', df['Position'])
df['Position'] = np.where(df['Player'] == 'Jeff Wilson', 'RB', df['Position'])
df['Position'] = np.where(df['Player'] == 'Tyler Allgeier', 'RB', df['Position'])
df['Position'] = np.where(df['Player'] == 'Latavius Murray', 'RB', df['Position'])
df['Position'] = np.where(df['Player'] == 'Taysom Hill', 'TE', df['Position'])
df['Position'] = np.where(df['Player'] == 'Evan Engram', 'TE', df['Position'])
df['Position'] = np.where(df['Player'] == 'Zay Jones', 'WR', df['Position'])
df['Position'] = np.where(df['Player'] == 'Christian Watson', 'WR', df['Position'])

R1 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 1)]
R2 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 2)]
R3 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 3)]
R4 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 4)]
R5 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 5)]
R6 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 6)]
R7 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 7)]
R8 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 8)]
R9 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 9)]
R10 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 10)]
R11 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 11)]
R12 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 12)]
R13 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 13)]
R14 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 14)]
R15 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 15)]
R16 = df[(df['TEAM'] == "Broncos Country Let's Ride") & (df['Round'] == 16)]




QB = 0
RB = 0
WR = 0
TE = 0
K = 0
DST = 0 
#round 1
max_step = df[(df['Used'] == 0) & (df['Number'] > R1['Number'].max()) & (df['Position'] == 'RB')]
max_fpts = max_step['FPTS/G'].max()
max_rows = df[df['FPTS/G'] == max_fpts]
max_rows = max_rows[(max_rows['Position'] == 'RB')]
max_rows = max_rows[(max_rows['Number'] > R1['Number'].max())]

R1['Player'] = max_rows['Player'].values
R1['FPTS/G'] = max_rows['FPTS/G'].values
R1['Position'] = max_rows['Position'].values

np.where(df['Player'] == str(max_rows['Player']), df['Used'] == 1, df['Used'] == 0)

x = (df['Player'] == str(max_rows['Player']))


