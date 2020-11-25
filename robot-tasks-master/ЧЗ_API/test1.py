from urllib import request, parse
import sys

myUrl= "https://www.google.com/search?"
value= {'q':'test'}

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl)
    otvet = request.urlopen(req)
    for line in otvet:
        print(line)

except Exception:
    print("ошибка")
    print(sys.exc_info()[1])