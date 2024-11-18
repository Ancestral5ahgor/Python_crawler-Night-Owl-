const CryptoJS = require("crypto-js");

const key = CryptoJS.enc.Utf8.parse("mysecretkey12345"); //十六位十六进制数作为秘钥
const iv = CryptoJS.enc.Utf8.parse("MyInitialization"); //十六位十六进制数作为秘钥偏移量

//Hook AES 加密
var _AES_ecrypt = CryptoJS.AES.encrypt;
CryptoJS.AES.encrypt = function (data, key, obj) {
    console.log("加密前:", data);
    // data = _AES_ecrypt(data, key, obj);
    return _AES_ecrypt(data, key, obj);
}


//加密函数
function encrypt(data) {
  const encrypted = CryptoJS.AES.encrypt(data, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  });
    return encrypted.toString();
}

//解密函数
function decrypt(data) {
  const decrypted = CryptoJS.AES.decrypt(data, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  });
  return decrypted.toString(CryptoJS.enc.Utf8);
}

var _AES_backup = CryptoJS.AES.decrypt
CryptoJS.AES.decrypt = function (data, key, obj) {
    debugger;
    console.log("Hook AES -- >> 解密前:", data);
    return _AES_backup(data, key, obj);
}


//加密
const data = "hello world";
const encrypted = encrypt(data);
console.log("加密:", encrypted);

//解密
const decrypted = decrypt(encrypted);
console.log("解密:", decrypted);