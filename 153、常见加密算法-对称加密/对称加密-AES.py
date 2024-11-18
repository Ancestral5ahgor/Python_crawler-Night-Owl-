# pycryptodome

# AES 、DES、3DES

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


# 加密
def aes_encrypt(key, iv, plain_text):
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    plain_text_pad = pad(plain_text, AES.block_size)
    cipher_text = cipher.encrypt(plain_text_pad)
    cipher_text_base64 = base64.b64encode(cipher_text).decode()
    return cipher_text_base64


# print(cipher_text, cipher_text_base64)

# 解密
# cipher_text_base64 = aes_encrypt(key, iv, plain_text)


def aes_decrypt(key, iv, cipher_text_base64):
    cipher_text = base64.b64decode(cipher_text_base64)

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    plain_text_unpad = cipher.decrypt(cipher_text)
    plain_text_ = unpad(plain_text_unpad, AES.block_size)
    return plain_text_.decode()
    # print(plain_text_.decode())


if __name__ == "__main__":

    key = b"0123456789abcdef"  # byte
    iv = b"0123456789abcdef"

    plain_text = "这是原始数据".encode()

    cipher_text_64 = aes_encrypt(key, iv, plain_text)

    decrpt_text = aes_decrypt(key, iv, cipher_text_64)

    print(decrpt_text)
