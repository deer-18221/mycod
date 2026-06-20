import os
import time
import hashlib
pas="b1e234b889cd5d26c700f851240fd359"
az=input('inter pass:')
se=az.encode()
dc=hashlib.md5(string=se)
ft=dc.hexdigest()
gb=ft.encode()
hu=hashlib.md5(string=gb)
jm=hu.hexdigest()
ko=jm.encode()
lp=hashlib.md5(string=ko)
cx=lp.hexdigest()
tt=str(cx)
if tt==pas:
    os.chdir("E:\\cod\\user")
    x=os.listdir()
    for i in x:
        os.remove(i)
        time.sleep(1)
        open(i,'w+')
       
else:
    True
