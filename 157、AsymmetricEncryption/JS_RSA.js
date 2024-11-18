window = global;
const JSEncrypt = require('jsencrypt')

const fs  = require('fs');

window.JSEncrypt = JSEncrypt

var public = fs.readFileSync('public_key.pem', 'utf8'); // get public key
var private = fs.readFileSync('private_key.pem', 'utf8'); // get private key

// Hook RSA
const org_setPublickey = JSEncrypt.prototype.setPublicKey;
JSEncrypt.prototype.setPublicKey = function(public) {
    console.log('Hook RSA设置公钥 --> ',public)
    org_setPublickey.call(this, public);
    this.public = public;
}

const org_setPrivateKey = JSEncrypt.prototype.setPrivateKey;
JSEncrypt.prototype.setPrivateKey = function(private) {
    console.log('Hook RSA设置私钥 --> ',private)
    org_setPrivateKey.call(this, private);
    this.private = private;
}


const org_encrypt = JSEncrypt.prototype.encrypt;
JSEncrypt.prototype.encrypt = function(plain_text) {
    console.log('Hook RSA加密前 明文 --> ',plain_text)
    cipher_text = org_encrypt.call(this, plain_text);
    this.plain_text = plain_text;
    return cipher_text;
}

const org_decrypt= JSEncrypt.prototype.decrypt;
JSEncrypt.prototype.decrypt = function(cipher_text) {
    console.log('Hook RSA解密前的密文 --> ',cipher_text)
    decode_text = org_decrypt.call(this, cipher_text);
    this.cipher_text = cipher_text;
    return decode_text;
}


plain_text = '这是明文';
cipher = new JSEncrypt();
cipher.setPublicKey(public)
cipher_text = cipher.encrypt(plain_text);

cipher.setPrivateKey(private)
decode_text = cipher.decrypt(cipher_text);

console.log('加密的数据：',cipher_text);
console.log('解密的数据：',decode_text);