#!/usr/local/bin/python2.7
from flask import Flask, render_template, json, jsonify, request
import MySQLdb
import pandas as pd
import numpy as np
import json


app = Flask(__name__)


@app.route('/api/food/',methods=['GET'])
def get_food():

    # Set up MySQL
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Wang8812321",  # your password
                     db="FlaskApp")        # name of the data base

    dbc  = db.cursor()

    db.set_character_set('utf8')
    dbc.execute('SET NAMES utf8;')
    dbc.execute('SET CHARACTER SET utf8;')
    dbc.execute('SET character_set_connection=utf8;')

    calories = request.args.get('calories')
    dinHall = request.args.get('dining')
    tags = request.args.get('tags')
    ban = request.args.get('ban')
    
    tlist = json.loads(tags)
    blist = json.loads(ban)
    llist = {"1": "Westend", "2": "Burger37", "3":"Deets","4":"D2", "5":"Dxpress", "6":"Grill_Owens", "7":"Turner", "8":"Vet_Cafe"}

    sql = "SELECT * FROM Food WHERE calories <= %s AND calories >= %s AND location LIKE '%s' " % (int(calories)+100, int(calories)-100, llist[dinHall], )
    
    for word in blist:
        sql = sql + "AND tag NOT LIKE '%s' AND allergen NOT LIKE '%s' " % ("%"+word+"%","%"+word+"%",)

    sql = sql + ";"

    dbc.execute(sql)

    data = dbc.fetchall()
    if data == ():
        return jsonify(id = [])
    df = pd.DataFrame(np.array(data))
    df.columns = ['food_id','food_name','serving_size','calories','fat_type','total_fat','sat_fat','trans_fat','cholesterol','sodium','protein','total_carbon','fiber','sugar','calcium','iron','vaiu','vc','meal','location','allergen','tag','ingredient',]


    df['weight'] = 0
    #return sql

    for i , row in df.iterrows():
        sum = 0
        for key,value in tlist.iteritems():
            if key in df.xs(i)['tag'] or key in df.xs(i)['allergen']:
                sum = sum + value
        c = abs(100 - (float(df.xs(i)['calories']) - float(calories)))
        df.loc[i, 'weight'] = sum*c 

    #df = df[df.weight!=0]   
    df = df.sort('weight',ascending=False)
    
    return jsonify(id = df['food_id'].tolist())


    
#
#SELECT * FROM Food WHERE calories < 200 AND allergen not like "%egg%" AND tag not like "%egg%" AND allergen not like "%milk%" AND tag not like "%milk%";


#   dbc.execute("SELECT * FROM Food WHERE calories <= %s AND calories >= %s AND location=%s", (int(calories)+100,int(calories)-100,dinHall,))
    # Data typically come in tuple form
#    data = dbc.fetchall()

#    df = pd.DataFrame(np.array(data))


#    arr = [123, 321, 456]
    #return df.to_html()
    

#@app.route('', methods=['GET'])
#def rec
#    mydata = json.load(request.get_json(force=True))
#
#    list = []
#    return list


#@app.route('/api/food/cal=<lm>'):
#def food_limit(lm):
#    dbc.execute("SELECT * FROM Food WHERE calories < %i", lm)
#    data = dbc.fetchall()
#    df = pd.DataFrame(np.array(data))
#    return df.to_html()

#@app.route('/api/food/rec', methods=['GET'])
#def rec():
#    file = request.json
#    json_object = json.load(file)
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<name>')
def users(name):
    return '<h1>helllllll000000o %s</h1>' % name

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
