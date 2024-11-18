# pycryptodome

# AES 、DES、3DES

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64


# 加密
def aes_encrypt(key, iv, plain_text):
    cipher = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)
    plain_text_pad = pad(plain_text, DES.block_size)
    cipher_text = cipher.encrypt(plain_text_pad)
    cipher_text_base64 = base64.b64encode(cipher_text).decode()
    return cipher_text_base64


# print(cipher_text, cipher_text_base64)

# 解密
# cipher_text_base64 = aes_encrypt(key, iv, plain_text)


def aes_decrypt(key, iv, cipher_text_base64):
    cipher_text = base64.b64decode(cipher_text_base64)

    cipher = DES.new(key=key, mode=DES.MODE_CBC, iv=iv)
    plain_text_unpad = cipher.decrypt(cipher_text)
    plain_text_ = unpad(plain_text_unpad, DES.block_size)  # 去填充
    return plain_text_.decode()
    # print(plain_text_.decode())


if __name__ == "__main__":

    key = b"01234567"  # byte
    iv = b"01234567"

    plain_text = "测试测试".encode()

    cipher_text_64 = aes_encrypt(key, iv, plain_text)

    decrpt_text = aes_decrypt(key, iv, cipher_text_64)

    print(decrpt_text)
