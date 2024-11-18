
// a = {a:function x(){console.log("1")},b:function x(){console.log("2")}}

// a.a()
// a.b()

!function(t){
    //加载器
    function e(s){
        // i 缓存
        if (i[s])
            return i[s].exports;
        //建立缓存
        var n = i[s] = {
            exports: {},
            id: s,
            loaded: !1
        };
        //
        return t[s].call(n.exports, n, n.exports, e), 
        n.loaded = !0, 
        n.exports
    }
    var i = {};
    // e('a')
    }({
        a:function(a,b,c){
            console.log("Function 0")
            c('b')
        },
        b:function(){
            console.log("Function 1")
        }
    })



