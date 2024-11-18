// 查看变量类型

// var a = 100
// console.log(typeof a)


// var a = undefined
// console.log(typeof a)

// var a = null;
// console.log(typeof a)

// if (undefined == null){
//     console.log("执行")
// }

//布尔类型
// var a = undefined , b=null
// console.log(Boolean(a),Boolean(b))

//数字类型
// var min_value = Number.MIN_VALUE
// var max_value = Number.MAX_VALUE
// console.log(min_value,max_value)
// 5e-324 1.7976931348623157e+308

//
// var a = 1/0;
// console.log(isFinite(a))

// var a =0/0;
// console.log(isNaN(a)) //not a number

// 数值转换
// var a = '逆向' , b = '1' , c = '3.14';
// console.log(Number(c))
// console.log(parseInt(c))
// console.log(parseFloat(c))

//十六进制转换
// var a = '0xFF';
// console.log(Number(a))

//字符串
// var a = 'hello' , b = "World",c = `你好`;
// console.log(a,b,c)

//转化字符转
// var s = 'abc', d = 'def';
// console.log(s+d)

// var a = 99 ,b = '1',c = 999
// console.log(a+b+c)
// 991999

//数组，列表
// var a = [1,3,5]
// console.log(a)
// console.log(""+a)
// // [ 1, 3, 5 ]
// // 1,3,5

// var s = 12345
// console.log(s.toString(),String(s))

// var s = null
// console.log(s + "")

// var s = 20
// console.log(`西瓜是：${s}元一斤`)

//字符串的操作
// var s = '逆向,真简单啊，你觉得呢！'
// console.log(s.substr(3,4))
// console.log(s.substring(3,6)) //3到6

// console.log(s.split(','))
// console.log(s.indexOf('啊'))
// console.log(s.lastIndexOf('你'))
// console.log(s.length)

S = 'Hello,World!'
// console.log(S.toUpperCase(),S.toLowerCase())
// console.log(S.charAt(0),S.charAt(1),S.charAt(2))
console.log(S.charCodeAt(0),S.charCodeAt(1),S.charCodeAt(2))
console.log(String.fromCharCode(72))

