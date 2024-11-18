// 保存原始Function引用
var originalFuntion = Function;

//Hook Function
Function = function(){
    var args = Array.prototype.slice.call(arguments);
    var containsDebugger = args.some(function(atg){
        return arg.indexOf('debugger') !== -1;
    });

    if (containsDebugger){
        console.log('Function(）调用包含debugger，返回空内容.');
        //返回一个空函数
        return function(){};
    }

    console.log('Function()调用参数:',args);
    //调用原始Function构造函数并返回结果
    return originalFuntion.apply(this,args);
};

//保护tostring方法
originalFuntion.toString = Function.toString;

//保存原始Function.constructor引用
var originalFuntionConstructor = Function.constructor;

//Hook Function.constructor
Function.constructor = function(){
    var args = Array.prototype.slice.call(arguments);
    var containsDebugger = args.some(function(atg){
        return arg.indexOf('debugger') !== -1;
    });

    if (containsDebugger){
        console.log('Function.constructor()调用包含debugger，返回空内容.');
        //返回一个空函数
        return function(){};
    }

    console.log('Function.constructor()调用参数:',args);
    //调用原始Function.constructor并返回结果
    return originalFuntionConstructor.apply(this,args);
};

//保护toString方法
originalFuntionConstructor.toString = Function.constructor.toString;

//测试Hook
var func1 = Function('console.log("func1");');
func1(); //输出：“func1”

var func2 = Function.constructor('console.log("func2");');
func2(); //输出：“func2”

var func3 = Function('debugger;');
func3(); //输出：“func3”

var func4 = Function.constructor('debugger;');
func4(); //输出：“func4”

