'use strict';
function dice_throw() {
  let number;
  number=Math.floor(Math.random()*6+1);
  return number;
}

const list=[];
let result;

do {
  result=dice_throw();
  list.push(result);
} while (result!==6)

for (let result of list) {
  document.querySelector('#answer').innerHTML+=`<li>${result}</li>`;
}