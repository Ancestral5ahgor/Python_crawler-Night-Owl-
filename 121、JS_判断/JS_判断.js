// JS判断

// i = 17
// if (i < 10 ){
//     console.log('i<10')
// }
// else if(i>10 && i<20){
//     console.log('i>10 && i<20')
// }
// else{
//     console.log('i>=10')
// }

// i = 14
// if (i < 10 ) console.log('i<10')
// else if(i>10 && i<20) console.log('i>10 && i<20')
// else console.log('i>=10')

// switch
// t = 10
// switch(t){
//     case 1:
        
//     case 2:
        
//     case 3:
        
//     case 4:
        
//     case 5:
//         console.log('工作日')
//         break;
//     case 6:
        
//     case 7:
//         console.log('非工作日')
//         break;
//     default:
//         console.log('输入错误')
// }

// x = 1
// x += 1
// console.log(x)

var s = [3 , 1, 2]
var i =0
while(true){
    switch(s[i++]){
        case 1:
            x +=1;
            break;
        case 2:
            console.log(x);
            return;
        case 3:
            x = 1;
            break;
    }
}

