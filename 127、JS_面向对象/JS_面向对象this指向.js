// window ----> global

// name ='perry'
// console.log(global.name == name)

// console.log(this)

// var name ='perry'
// function test(){
//     console.log(this.name)
// }
// test()

//对象
t = {
    name:'perry',
    teach:function(){
        console.log(this.name)
    }
}

console.log(t.teach())
