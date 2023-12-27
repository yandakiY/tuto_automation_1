import pandas as pd

results = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

print(results)

# update colums

results.rename(columns={'Date':'Jour du match' , 'HomeTeam':'Equipe a domicile'} , inplace=True)

print(results)