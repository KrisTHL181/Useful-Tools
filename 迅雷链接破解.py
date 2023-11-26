import base64
def crack(url):
    strb=url.lstrip('thunder://')
    urlb=base64.b64decode(strb)
    strurl=urlb.decode('utf-8')
    zsrul=strurl.strip('AAZZ')
    print(zsrul)
while True:
    try:crack(input("迅雷链接:"))
    except BaseException:print("解析错误!")
