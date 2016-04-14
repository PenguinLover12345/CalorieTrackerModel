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

def recommendNoPreference(currentCalorieMeal, diningHall, preference):
    goal = "SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i UNION SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i ORDER by ABS(%i - calories)"

    cnx = mysql.connector.connect(user='admin', database='diningHall')
    cursor = cnx.cursor()
    cursor.execute(goal, (diningHall, currentCalorieMeal-100, currentCalorieMeal, diningHall, currentCalorieMeal, currentCalorieMeal+100, currentCalorieMeal))

    #add stuff with cursors --- https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    #http://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
    
    recommendations = pd.Dataframe(cursor.fetchall())
    
    return recommendations
    

def recommend(currentCalorieMeal, diningHall, preference):
      
      
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

    recommendations = pd.Dataframe(cursor.fetchall())

    return recommendations
    

def parseTag():
    tag = 3 #list of tags obtained from database
    

main()