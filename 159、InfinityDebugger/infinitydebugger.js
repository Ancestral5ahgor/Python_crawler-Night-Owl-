 
//hook eval

const originalEval = eval;

 function hookedEval(code){
    if(code.includes('debugger')){
        console.log('Hook eval....')
        code = code.replace('debugger;','');

    }
    return originalEval(code);
 }

eval = hookedEval;
    
