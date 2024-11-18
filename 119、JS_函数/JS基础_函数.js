// JS基础 - 函数

// function test(a) {
//     return a
// }

// var b = test(1)
// console.log(b)

// 匿名函数
// var a = function(){
//     console.log('匿名函数')
// }

// a()

// a = [
//     function(){console.log('初始化')},
//     function(){console.log('点击登陆')},
//     function(){console.log('开始加密')},
//     function(){console.log('发送数据')},
//     function(){console.log('结束')},
// ]

// a.push(function(){console.log('倒数')})
// a.shift()

// for (i = 0; i < a.length; i++) {
//     a[i]()
// }
        

// function test () {
//     console.log('test')
// }

// function b(m){
//     m()
// }

// b(function(){console.log('倒数')})

// function tt () {
//     var a =1 ,b =2
//     return a+2 , 
//     b-- , 
//     b-1
// }

// console.log(tt())

// function test () {
//     a = arguments
//     console.log(a)
//     console.log('逆向真简单')
// }

// test = 100
// console.log(test)
// // test(2,3,4)

// 自执行函数
// (function(){
//     console.log('函数被执行了1')
// })();

// (function(){
//     console.log('函数被执行了2')
// }());

// !function(){
//     console.log('函数被执行了3')
// }()

//函数提升
function eat(){
    console.log('吃麦当劳')
}

eat()

function eat(){
    console.log('吃拉面')
}

eat()
