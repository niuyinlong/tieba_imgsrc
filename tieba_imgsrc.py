import urllib.request
import re
import ssl
from urllib.parse import urljoin

ssl._create_default_https_context = ssl._create_unverified_context
timg = urllib.request.urlopen('http://tieba.baidu.com/p/6224828650')
print(timg)
niu = timg.read().decode("utf-8")
listurl = re.findall(r'//imgsrc[^\s]*\.jpg',niu)
i = 1
for url in listurl:
    f = open(str(i)+'.jpg','wb')
    print(f)
    timg = urllib.request.urlopen('http:'+url)
    print(timg)
    niu = timg.read()
    f.write(niu)
    if i == 3:
    	break

    i+=1