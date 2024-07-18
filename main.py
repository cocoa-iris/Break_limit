import requests
import json
url=input('url : ')
tex=requests.get(url)
yuke=tex.text
dat=yuke.find('<a href="')
new=yuke[dat:]
dat2=new.find('>')
dat3=new.find('</div>')
honbun=new[dat2:dat3]
newtext=honbun.replace('<br>','\n')
print(newtext)
