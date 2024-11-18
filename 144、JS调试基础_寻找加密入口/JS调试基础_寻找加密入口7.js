(function(){
    'use strict';
    var cookieTemp = '';
    Object.defineProperty(document, 'cookie', {
        set: function(value){
            if(value.indexOf('_dfp')!=-1){
                debugger;
            }
            // cookieTemp = value;
            console.log('Hook捕获到cookie设置',value);
            cookieTemp = value;
            return value;
        },
        get: function(){
            return cookieTemp;
        },
    });
})();

// Hook注入
// 注入工具
// 浏览器手动注入
// 只能Hook全局变量
// 找到第一个JS加载文件位置打断点
// 事件监听load - > on load 打断点
