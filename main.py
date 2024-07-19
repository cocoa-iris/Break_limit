import requests
import json
url=input('url : ')
tex=requests.get(url)
yuke=tex.text
dat=yuke.find('<')
new=yuke[dat:]
dat2=new.find('曲名')
dat3=new.find('')
honbun=new[dat2:]
newtext=honbun.replace('<br>','\n').replace('<div>','').replace('<br />','')\
.replace('</div>','').replace('<li>','-')
print(newtext)
