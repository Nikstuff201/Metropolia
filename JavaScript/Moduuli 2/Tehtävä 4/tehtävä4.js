'use strict';
const list=[];
let number;
number=parseInt(prompt('Give your number'));

while (number!==0) {
  list.push(number);
  number=parseInt(prompt('Give your number'));
}

list.sort((a,b)=>b-a);

for (let number of list){
  console.log(number);
}