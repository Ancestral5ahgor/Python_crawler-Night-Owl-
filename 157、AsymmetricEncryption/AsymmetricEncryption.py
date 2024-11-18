from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.public_key().export_key()
    with open("private_key.pem", "wb") as f:
        f.write(private_key)
    with open("public_key.pem", "wb") as f:
        f.write(public_key)
    return private_key, public_key


def rsa_encrypt():
    key = RSA.import_key(private_key)
    cipher = PKCS1_v1_5.new(key)
    cipher_text = cipher.encrypt(plain_text)
    return base64.b64encode(cipher_text)
    # print(cipher_text)


def rsa_decrypt(private_key, cipher_text_base64):
    key = RSA.import_key(private_key, cipher_text_base64)
    cipher = PKCS1_v1_5.new(key)
    cipher_text = base64.b64decode(cipher_text_base64)
    decode_text = cipher.decrypt(cipher_text, None)
    return decode_text.decode()
    # print(decode_text)


def rsa_encrypt(public_key, plain_text):
    key = RSA.import_key(public_key)
    cipher = PKCS1_v1_5.new(key)
    cipher_text = cipher.encrypt(plain_text)
    return base64.b64encode(cipher_text)
    # print(cipher_text)


if __name__ == "__main__":
    plain_text = "明文".encode()
    private_key, public_key = generate_key_pair()
    cipher_text_base64 = rsa_encrypt(public_key, plain_text)
    decode_text = rsa_decrypt(private_key, cipher_text_base64)
    print(cipher_text_base64)
    print(decode_text)


# def rsa_decrypt():
#     key = RSA.import_key(private_key)
#     cipher = PKCS1_v1_5.new(key)
#     with open("encrypted.txt", "rb") as f:
#         encrypted = f.read()
#     decrypted = cipher.decrypt(encrypted, 32)
#     with open("decrypted.txt", "wb") as f:
#         f.write(decrypted)


# def encrypt():
#     key = RSA.import_key(public_key)
#     encrypted = key.encrypt(plain_text, 32)
#     with open("encrypted.txt", "wb") as f:
#         f.write(encrypted[0])


# def encrypt():
#     with open("public_key.pem", "rb") as f:
#         key = RSA.import_key(f.read())
#     with open("message.txt", "rb") as f:
#         message = f.read()
#     encrypted = key.encrypt(message, 32)
#     with open("encrypted.txt", "wb") as f:
#         f.write(encrypted[0])


# def decrypt():
#     with open("private_key.pem", "rb") as f:
#         key = RSA.import_key(f.read())
#     with open("encrypted.txt", "rb") as f:
#         encrypted = f.read()
#     decrypted = key.decrypt(encrypted)
#     with open("decrypted.txt", "wb") as f:
#         f.write(decrypted)


# if __name__ == "__main__":
#     generate_key_pair()
#     encrypt()
#     decrypt()
