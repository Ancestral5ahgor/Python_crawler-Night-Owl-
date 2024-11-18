# base64编码解码
import base64

# 字符串编码和解码 ascii，utf-8，gbk
s = '中文'.encode('utf-8') # b-->byte字节 \x 十六进制
s1 = '中文'.encode('gbk')

# print(s.decode(),s1)

s_64 = base64.b64encode(s)

s_64_decode = base64.b64decode(s_64)

print(s_64_decode.decode())




