const CryptoJS = require('crypto-js');

//hook md5
var md5_backup = CryptoJS.MD5
CryptoJS.MD5 = function(s){
    console.log('MD5 HOOK -- > 加密前的数据:' + s)
    return md5_backup(s)
}

s = '123456'
encrypt_s = CryptoJS.MD5(s).toString()
// encrypt_s1 = CryptoJS.SHA1(s).toString()

console.log(encrypt_s)



