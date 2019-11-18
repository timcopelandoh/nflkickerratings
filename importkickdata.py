import pandas as pd
import datetime

# Function to convert date from the given format (a string with the format mm/dd/yy) 
# to python date format.
def convert_date(x):
    x = x.split('/')
    return datetime.date(int('20'+x[2]), int(x[0]), int(x[1]))

# Function that imports and cleans kick data
def loadkickdata(filepath):
	kicks = pd.read_csv(filepath, header=0)

	# Rename column containing an @ symbol if the kicking team is the away team.
	kicks.rename(columns={'Unnamed: 3':'At'}, inplace=True)

	# Delete index column in csv
	del kicks['Rk']

	# Create boolean column if kicking team is the home team
	kicks['Home'] = (kicks['At'] != '@')

	# Isolate unique player id
	kicks['PlayerID'] = kicks['Player'].apply(lambda x: str.split(x, '\\')[1])

	# And player name
	kicks['Player name'] = kicks['Player'].apply(lambda x: str.split(x, '\\')[0])

	# Create variable for team whose stadium the game is played at
	kicks['Stadium'] = kicks.apply(lambda x: [x['Opp'],x['Tm']][x['Home']], axis='columns')

	# Reformat 'Good?' column to be a boolean
	kicks['Good?'] = (kicks['Good?']=='Y')

	# Reformat blocked kick column to be a boolean
	kicks['Blk?'] = (kicks['Blk?']=='Y')

	# Reformat date column
	kicks['Date'] = kicks['Date'].apply(convert_date)
	kicks['Dist_sq'] = kicks['Dist'].apply(lambda x: x**2)
	kicks['Season'] = kicks['Date'].apply(lambda x: x.year)
	kicks['Month'] = kicks['Date'].apply(lambda x: x.month)
	kicks['Constant'] = 1
	return kicks

	# Create variable for distance squared
	

	# Create variable 
	

	

