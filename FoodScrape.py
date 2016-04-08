import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import mysql.connector
from sqlalchemy import create_engine


urlh = "http://foodpro.dsa.vt.edu/FoodPro.NET/"
dtdate = str(datetime.date.today()).split("-")
fff = lambda x: 'None' if x == None else x.text
df = pd.DataFrame(columns=('food_name', 'serving_size', 'calories','fat_type',
    'total_fat','sat_fat','trans_fat','cholesterol','sodium','protein',
    'total_carbon','fiber','sugar','calcium','iron','vaiu','vc','ingredient','meal'))
df1 = df
df2 = df
df3 = df
df4 = df
df5 = df
df6 = df
df7 = df

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
    if s!=[] :
        df = df.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'all'
        }, ignore_index=True)
    print i
df.to_csv('Westend.csv', sep=',', encoding='utf-8')


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
    if s!=[] :
        df1 = df1.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'all'
        }, ignore_index=True)
    print i
df1.to_csv('Burger_37.csv', sep=',', encoding='utf-8')


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
    if s!=[] :
        df2 = df2.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'all'
        }, ignore_index=True)
    print i
df2.to_csv('Deets.csv', sep=',', encoding='utf-8')


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
    if s!=[] :
        df3 = df3.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'breakfast'
        }, ignore_index=True)
    print i
    
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
    if s!=[] :
        df3 = df3.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'lunch'
        }, ignore_index=True)
    print i 

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
    if s!=[] :
        df3 = df3.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'dinner'
        }, ignore_index=True)
    print i     
    
df3.to_csv('D2.csv', sep=',', encoding='utf-8')




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
    if s!=[] :
        df4 = df4.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'breakfast'
        }, ignore_index=True)
    print i
    
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
    if s!=[] :
        df4 = df4.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'lunch & dinner'
        }, ignore_index=True)
    print i 
    
df4.to_csv('Dxpress.csv', sep=',', encoding='utf-8')



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
    if s!=[] :
        df5 = df5.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'all'
        }, ignore_index=True)
    print i 
    
df5.to_csv('Owens.csv', sep=',', encoding='utf-8')



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
    if s!=[] :
        df6 = df6.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'breakfast'
        }, ignore_index=True)
    print i
    
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
    if s!=[] :
        df6 = df6.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'lunch & dinner'
        }, ignore_index=True)
    print i 
    
df6.to_csv('Turner.csv', sep=',', encoding='utf-8')




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
    if s!=[] :
        df7 = df7.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'breakfast'
        }, ignore_index=True)
    print i
    
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
    if s!=[] :
        df7 = df7.append({
        'food_name': soupi.find('div',{'class':'labelrecipe'}).text,
        'serving_size': s[1],
        'calories':s[2].split(u'\xa0')[1],
        'fat_type':s[3].split(u'\xa0')[-1],
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
        'ingredient': fff(soupi.find('span',{'class':'labelingredientsvalue'})),
        'meal':'lunch'
        }, ignore_index=True)
    print i 
    
df7.to_csv('Vet_Cafe.csv', sep=',', encoding='utf-8')

