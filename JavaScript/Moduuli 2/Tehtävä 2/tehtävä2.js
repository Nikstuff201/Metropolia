'use strict'
const nop=parseInt(prompt('Give number of participants'));
const list=[];
for (let i=1;i<=nop;i++) {
  list.push(prompt('Give the name of participant'));
}

list.sort();

for (let name of list) {
document.querySelector('#answer').innerHTML+=`<li>${name}</li>`;
  }