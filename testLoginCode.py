#encoding=utf-8
import requests
import sys
from PIL import Image
import io
io.StringIO
print(sys.getfilesystemencoding())
req=requests.get("http://10.80.73.7/IISP//identiryCode/getIdentiryCode?timestamp=1501119138854")
respHtml=req.text.encode('utf-8')
print(respHtml)
# img = Image.open(io.StringIO(respHtml))
# img.show()

# print(req.text.encode('utf-8'))

# def getUrlRespHtml(url,head) :
#     resp = getUrlResponse(url,head)
#     respHtml = resp.read()
#     return respHtml 
    
# def getCheckCode(url,postdic,headerdic):
#     print "+"*20+"getCheckCode"+"+"*20
# #    response = urllib2.urlopen(url)
#     respHtml = getUrlRespHtml(url,headerdic)
#     img = Image.open(cStringIO.StringIO(respHtml))
#     img.show()
#     checkCode = raw_input("code：") 
#     print 'aaa'
#     postdic["ValidateCode"] = checkCode
#     return postdic