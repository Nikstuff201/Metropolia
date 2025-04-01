'use strict';
const numero=parseInt(prompt('Give your number'));
let answer=true
if (numero>2){
  for(let i=2; i<numero; i++){
    if (numero%i==0){
      answer=false;
      break;
    }
    }
}
else if (numero==1){
  answer=false;
}
else if (numero==2){
  answer=true
}


if (answer==true){
  document.querySelector('#answer').innerHTML=`${numero} is a prime number`;
}
else {
  document.querySelector('#answer').innerHTML=`${numero} is not a prime number`;
}
