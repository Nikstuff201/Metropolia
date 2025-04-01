'use strict';
const throws=parseInt(prompt('Give the number of throws'));
let number,sum=0;
for (let i=1;i<=throws;i++) {
  number=Math.floor((Math.random()*6)+1);
  sum+=number;
}
document.querySelector('#summa').innerHTML=`${sum}`;