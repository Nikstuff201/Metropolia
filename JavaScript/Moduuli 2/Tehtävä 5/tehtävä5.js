'use strict';
const list=[];
let number
number=parseInt(prompt('Give your number'));

while (list.includes(number)!==true) {
  list.push(number);
  number=parseInt(prompt('Give your number'));
}

list.sort((a,b)=>a-b);

document.querySelector('#answer').innerHTML=`Number ${number} is already had been given`;

for (let num of list) {
  console.log(num)
}