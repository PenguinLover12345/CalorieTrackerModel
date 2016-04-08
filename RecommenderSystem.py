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

def recommend(currentCalorieMeal, meal, diningHall):
    goal = "SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i UNION SELECT * FROM %s WHERE 'calories' >= %i AND 'calories' <= %i ORDER by ABS(%i - calories)"

    cnx = mysql.connector.connect(user='admin', database='employees')
    cursor = cnx.cursor()
    cursor.execute(goal, (diningHall, meal-100, meal, diningHall, meal, meal+100, meal))

    #add stuff with cursors --- https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    #http://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
    
    recommendations = pd.Dataframe(cursor.fetchall())
    
    return recommendations
     #for row in diningHallInformation:
#s          if row[3] 
      #Instead of searching csv, we could do a select statement in SQL such that
      #we select meals that are in a calorie limit.  Should we have it as a ranking
      #system? limited ranking system?  
      
    
    
main()