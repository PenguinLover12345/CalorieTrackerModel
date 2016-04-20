import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import mysql.connector
from sqlalchemy import create_engine


#with open('westend.csv', 'rb') as csvfile:
#    diningHallInformation = csv.reader(csvfile, csvfile, delimiter=' ', quotechar='|')
    
def main():
    x = 0

#def recommendNoPreference(currentCalorieMeal, diningHall, preference):
#    goal = "SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i UNION SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i ORDER by ABS(%i - calories)"

#    cnx = mysql.connector.connect(user='admin', database='diningHall')
#    cursor = cnx.cursor()
#    cursor.execute(goal, (diningHall, currentCalorieMeal-100, currentCalorieMeal, diningHall, currentCalorieMeal, currentCalorieMeal+100, currentCalorieMeal))

    #add stuff with cursors --- https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    #http://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
    
#    recommendations = pd.Dataframe(cursor.fetchall())
    
#    return recommendations
    
def recommend(currentCalorieMeal, diningHall, preference, bans):
      
#Algorithm

# get preference list, p
# get goal and filter out what is not in the goal
# 
# each item's weight : sum(t(i) * p(i)) + abs(cal - goal) / j
# where each t is a tag the item has and j is the total number of tags an item 
# has
# 

    goal = "SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i ORDER by ABS(%i - calories)"

    cnx = mysql.connector.connect(user='admin', database='diningHall')
    cursor = cnx.cursor()
    cursor.execute(goal, (diningHall, currentCalorieMeal-100, currentCalorieMeal, diningHall, currentCalorieMeal, currentCalorieMeal+100, currentCalorieMeal))

    df = pd.Dataframe(cursor.fetchall())
    
    df['weight'] = 0
    banned = []
    
    
#    ----------LOOK HERE--------
    #do this in SQL
    for i in bans: #find list of banned foods
        for j, row in df.iterrows():
            if i in df.xs(j)['ingredients']:
                banned.append(df.xs(j))      # add all banned foods into a list
    df = df[~df.isin(banned)].dropna()       #remove everything that is banned from main dataframe
                                             #ask zhang is this is right/better way of doing this

    for i, row in df.iterrows():  #calculate weight for each food item
        sum = 0
        for key, value in preference.iteritems():    #key value for each preference
            if key in df.xs(i)['tag'] or key in df.xs(i)['allergen']:
                sum = sum + key                     #add weight for each preference
        c = abs(100 - (df.xs(i)['calories'] - currentCalorieMeal))      #add number to how close it is to calorie goal
        df.xs(i)['weight'] = sum * c   
    
    df.sort_values(['weight'], ascending=[False]) #sort descending order by highest weight

#--------------------END LOOKING------
    return df
                
                

#r = request.get_json()
#r = 3
cal = r["calories"]

banlist = []
for b in r["bans"]: #create list of bans
    banlist.append(b)

#dict = {'milk':0, 'wheat':0, 'soy':0, 'cheese':0, 'egg':0, 'beef':0, 'turkey':0, 'chicken':0, 'pork':0, 'peanuts':0, 'veggie':0, 'pizza':0, 'lamb':0, 'onion':0, 'tomato':0, 'cream':0, 'pepper':0, 'shellfish':0, 'gluten':0};
dict = {}

for d in r["dict"]: #update preference list
    dict.update (d)



main()