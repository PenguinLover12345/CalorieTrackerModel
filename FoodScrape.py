import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import MySQLdb


urlh = "http://foodpro.dsa.vt.edu/FoodPro.NET/"
dtdate = str(datetime.date.today()).split("-")

fff = lambda x: 'None' if x == None else x.text

taglist = [
'milk',
'wheat',
'soy',
'cheese',
'egg',
'beef',
'turkey',
'chicken',
'pork',
'peanuts',
'veggie',
'pizza',
'lamb',
'onion',
'tomato',
'cream',
'pepper',
'shellfish',
'gluten',
]

df0 = pd.DataFrame(columns=('food_id','food_name', 'serving_size', 'calories','fat_type',
    'total_fat','sat_fat','trans_fat','cholesterol','sodium','protein',
    'total_carbon','fiber','sugar','calcium','iron','vaiu','vc','meal','location','allergen','tag','ingredient'))
df1 = df0
df2 = df0
df3 = df0
df4 = df0
df5 = df0
df6 = df0
df7 = df0

loc = 10000

url = "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=16&locationName=WEST+END+MKT+AT+COCHRANE+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Daily+Items"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]
for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df0 = df0.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast & lunch & dinner',
        'location': 'Westend',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
df0.to_csv('Datasets/Westend.csv', sep=',', encoding='utf-8', index=False)

loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=18&locationName=BURGER+%2737+AT+SQUIRES&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Daily+Items"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')

foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]
for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df1 = df1.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast & lunch & dinner',
        'location': 'Burger37',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
df1.to_csv('Datasets/Burger_37.csv', sep=',', encoding='utf-8', index=False)

loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=07&locationName=DEET%27S+PLACE++AT+DIETRICK&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Daily+Items"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df2 = df2.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast & lunch & dinner',
        'location': 'Deets',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
df2.to_csv('Datasets/Deets.csv', sep=',', encoding='utf-8', index=False)

loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=15&locationName=D2+AT+DIETRICK+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Breakfast"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df3 = df3.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast',
        'location': 'D2',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
    
url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=15&locationName=D2+AT+DIETRICK+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Lunch"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df3 = df3.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'lunch',
        'location': 'D2',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1 

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=15&locationName=D2+AT+DIETRICK+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Dinner"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df3 = df3.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'Dinner',
        'location': 'D2',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1     
    
df3.to_csv('Datasets/D2.csv', sep=',', encoding='utf-8', index=False)

loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=13&locationName=DXPRESS+AT+DIETRICK+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Breakfast"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df4 = df4.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast',
        'location':'Dxpress',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
    
url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=13&locationName=DXPRESS+AT+DIETRICK+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Lunch+%26+Dinner"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df4 = df4.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'lunch & dinner',
        'location':'Dxpress',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1 
    
df4.to_csv('Datasets/Dxpress.csv', sep=',', encoding='utf-8', index=False)

loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=09&locationName=FOOD+CRT%2f+HOKIE+GRILL+AT+OWENS+&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Daily+Items"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df5 = df5.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast & lunch & dinner',
        'location':'Grill_Owens',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1 
    
df5.to_csv('Datasets/Grill_Owens.csv', sep=',', encoding='utf-8',index=False)

loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=14&locationName=TURNER+PLACE+AT+LAVERY+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Breakfast"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df6 = df6.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast',
        'location':'Turner',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
    
url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=14&locationName=TURNER+PLACE+AT+LAVERY+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Lunch+%26+Dinner"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df6 = df6.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'lunch & dinner',
        'location':'Turner',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1 
    
df6.to_csv('Datasets/Turner.csv', sep=',', encoding='utf-8',index=False)


loc += 10000

url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=19&locationName=VET+MED+CAFE++AT+VMRCVM+&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Breakfast"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df7 = df7.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'breakfast',
        'location':'Vet_Cafe',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1
    
url= "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=19&locationName=VET+MED+CAFE++AT+VMRCVM+&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate="+dtdate[1]+"%2f"+dtdate[2]+"%2f"+dtdate[0]+"&mealName=Lunch"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')
foodl = soup.find_all('div', {"class":'longmenucoldispname'})
href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
    ingr = fff(soupi.find('span',{'class':'labelingredientsvalue'}))
    allg = fff(soupi.find('span',{'class':'labelallergensvalue'}))
    tags = []
    if ingr != 'None':
        inglist = "".join(c for c in ingr.lower() if c not in (',','.','?','!',';',':',')','(')).split(" ")
        for word in inglist:
            if (word in taglist) and (not word in tags) :
                tags.append(word)
    tag = "None"
    if tags != [] :
        tag = "".join(x+", " for x in tags)
    if (len(s)==4 and len(n)==35 and len(v)==13) :
        df7 = df7.append({
        'food_id': loc+i+1,
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories': int(s[2].split(u'\xa0')[1]),
        'fat_type': s[3].split(u'\xa0')[-1],
        'total_fat': n[1].text,
        'sat_fat': n[9].text,
        'trans_fat': n[17].text,
        'cholesterol': n[23].text,
        'sodium': n[30].text,
        'protein': n[27].text,
        'total_carbon': n[5].text,
        'fiber': n[13].text,
        'sugar': n[20].text,
        'calcium': v[6].text.split(u'\xa0')[-1],
        'iron': v[8].text.split(u'\xa0')[-1],
        'vaiu': v[10].text.split(u'\xa0')[-1],
        'vc': v[12].text.split(u'\xa0')[-1],
        'meal':'lunch',
        'location':'Vet_Cafe',
        'allergen': allg,
        'tag': tag,
        'ingredient': ingr,
        }, ignore_index=True)
    print loc+i+1 
    
df7.to_csv('Datasets/Vet_Cafe.csv', sep=',', encoding='utf-8',index=False)



db  = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Wang8812321",  # your password
                     db="FlaskApp")        # name of the data base

dbc = db.cursor()

db.set_character_set('utf8')
dbc.execute('SET NAMES utf8;')
dbc.execute('SET CHARACTER SET utf8;')
dbc.execute('SET character_set_connection=utf8;')


df = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7])


df.to_sql(con=db,name='Food',if_exists='replace', flavor='mysql',index=False)

print "Finished"
