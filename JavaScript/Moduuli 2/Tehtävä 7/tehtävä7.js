'use strict';
function dice_throw(nos) {
  let number;
  number=Math.floor(Math.random()*nos+1);
  return number;
}

const nos=parseInt(prompt('Give the number of sides'));
const list=[];
let result;

do {
  result=dice_throw(nos);
  list.push(result);
} while (result!==nos)

for (let result of list) {
  document.querySelector('#answer').innerHTML+=`<li>${result}</li>`;
}