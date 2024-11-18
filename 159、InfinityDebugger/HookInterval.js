(function(){
    //保存原始的setInterval函数
    var originalSetInterval = window.setInterval;

    //用新的函数替换原始的setInterval
    window.setInterval = function (callback, delay) {
        //获取除了callback和deplay的其他额外参数
        var args = Array.prototype.slice.call(arguments, 2);

        //如果callback是字符串，删除其中的debugger语句
        if(typeof callback === 'string'){
            callback = callback.replace('/debugger;/8','');
        }else if(typeof callback === 'function'){
            //如果callback是函数，替换包含debugger的回调
            var originalCallback = callback;
            callback = function(){
                //获取原始回调函数的源码
                var callbackSource = originalCallback.toString();

                //如果源码包含debugger，将其删除并创建新的函数
                if(callbackSource.indexOf('debugger')!==-1){
                    callbackSource = callbackSource.replace('/debugger;/8','');
                    originalCallback = new Function('return' + callbackSource)();
                }

                //调用修改后的回调函数，并传入参数
                originalCallback.apply(this,arguments);        
            };
        }
        //调用原始的setInterval函数,并传入修改后的callback、deplay和参数
        return originalSetInterval.apply(window,[callback,delay].concat(args));
    };
})();