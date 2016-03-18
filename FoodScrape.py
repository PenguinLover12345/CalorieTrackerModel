import urllib
from bs4 import BeautifulSoup as bs
import pandas as pd


df = pd.DataFrame(columns=('food_name', 'serving_size', 'calories','fat_type',
    'total_fat','sat_fat','trans_fat','cholesterol','sodium','protein',
    'total_carbon','fiber','sugar','calcium','iron','vaiu','vc','ingredient'))


urlh = "http://foodpro.dsa.vt.edu/FoodPro.NET/"
url = "http://foodpro.dsa.vt.edu/FoodPro.NET/longmenu.aspx?sName=Virginia+Tech+Dining+Services&locationNum=16&locationName=WEST+END+MKT+AT+COCHRANE+HALL&naFlag=1&WeeksMenus=This+Week%27s+Menus&dtdate=02%2f08%2f2016&mealName=Daily+Items"
html = urllib.urlopen(url).read()
soup = bs(html,'html5lib')
soup.prettify().encode('UTF-8')

foodl = soup.find_all('div', {"class":'longmenucoldispname'})

#foodname = [f.text for f in foodl]

href = [f.find('a')['href'] for f in foodl]

for i in range(0,len(href)):
    urli = urlh + href[i]
    htmli = urllib.urlopen(urli).read()
    soupi = bs(htmli,'html5lib')
    soupi.prettify().encode('UTF-8')
    s = [f.text for f in soupi.find_all('font',{'size':'5'})]
    n = soupi.find_all('font',{'size':'4'})
    v = soupi.find_all('font',{'size':'3'})
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
    'ingredient': soupi.find('span',{'class':'labelingredientsvalue'}).text,
    }, ignore_index=True)
    print i

df.to_csv('output.csv', sep=',', encoding='utf-8')