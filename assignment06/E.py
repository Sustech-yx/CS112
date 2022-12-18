import pandas as pd
import numpy as npy

tmp_l = []
games = {'t1': [], 'n1': [], 't2': [], 'n2': []}
for _ in range(6):
    line = input().split(',')
    games['t1'].append(line[0])
    tmp_l.append(line[0])
    games['n1'].append(int(line[1]))
    games['t2'].append(line[2])
    games['n2'].append(int(line[3]))

games = pd.DataFrame(games)
score = pd.DataFrame({'team': list(set(tmp_l)), 'score': npy.zeros(4, dtype=npy.int16)
                                                , 'GD': npy.zeros(4, dtype=npy.int16)
                                                , 'GT': npy.zeros(4, dtype=npy.int16)})
# print(score.dtypes)

for _, row in games.iterrows():
    t1, n1, t2, n2 = row
    if n1 == n2:
        score.loc[score['team'] == t1, 'score'] += 1
        score.loc[score['team'] == t2, 'score'] += 1
    elif n1 > n2:
        score.loc[score['team'] == t1, 'score'] += 3
    else:
        score.loc[score['team'] == t2, 'score'] += 3
    score.loc[score['team'] == t1, 'GT'] += n1
    score.loc[score['team'] == t2, 'GT'] += n2
    score.loc[score['team'] == t1, 'GD'] += n1 - n2
    score.loc[score['team'] == t2, 'GD'] += n2 - n1

score = score.sort_values(by=['score', 'GD', 'GT'], ascending=[False, False, False], kind='stable')
for team in score['team']:
    print(team)
