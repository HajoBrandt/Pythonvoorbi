import requests
from bs4 import BeautifulSoup

url = 'https://www.practicepython.org/assets/Training_01.txt'
r = requests.get(url)
r = r.text
#print(str(r))
soup = BeautifulSoup(r, features='lxml')

txt = soup.find('p')
textStr = txt.text
textList = textStr.splitlines()
#print(textList[88])
categories = []
for x in textList:
    temp = x.split('/')
    categories.append(temp[2])
#rint(categories)
uniqueValues = []
[uniqueValues.append(x) for x in categories if x not in uniqueValues]
print(uniqueValues)
dic = {}
for x in uniqueValues:
    count = 0
    for y in categories:
        if y == x:
            count += 1
    dic[x] = (count)
print(dic)
file_object  = open("writefiles/categories.txt", "w+")
for x in dic:
    file_object.write(x + ':' + str(dic[x]) + '\n')
file_object.close
#print(txt.text)