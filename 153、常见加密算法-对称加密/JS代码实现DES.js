const cryptoJs = require("crypto-js");
const CryptoJS = require("crypto-js");



//Hook AES 加密
var _DES_ecrypt = CryptoJS.DES.encrypt;
CryptoJS.DES.encrypt = function (mes, key, obj) {
    console.log("加密前:", mes);
    // data = _AES_ecrypt(data, key, obj);
    return _DES_ecrypt(mes, key, obj);
}


//加密函数
function encrypt(mes,key) {
  const keyHex = CryptoJS.enc.Utf8.parse(key);
  const encrypted = CryptoJS.DES.encrypt(mes, keyHex, {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
  });
    return encrypted.toString();
}
var _DES_backup = CryptoJS.DES.decrypt
cryptoJs.DES.decrypt = function (mes, key, obj) {
    debugger;
    console.log("Hook DES 解密前 -- >> :", mes);
    return _DES_backup(mes, key, obj);
}

//解密函数
function decrypt(mes,key) {
  const keyHex = CryptoJS.enc.Utf8.parse(key);
  const decrypted = CryptoJS.DES.decrypt(mes, keyHex, {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
  });
  return decrypted.toString(CryptoJS.enc.Utf8);
}

cipher_text = encrypt("hello world","12345678");
console.log(decrypt(cipher_text,"12345678"))