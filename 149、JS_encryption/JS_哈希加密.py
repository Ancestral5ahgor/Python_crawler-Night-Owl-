from hashlib import md5,sha1,sha256,sha512

# obj = md5()
# obj = sha256()
obj = sha512()

text = '这是要加密的原始数据'.encode('utf-8')
# print(text)

obj.update(text)
encrypt_text = obj.hexdigest() #转为16进制的数据

print(encrypt_text,len(encrypt_text))
