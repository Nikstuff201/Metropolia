'use strict';
const list=[];
for (let i=1;i<=6;i++) {
  list.push(prompt('Give the name of a dog'));
}

list.sort();
list.reverse();

for (let name of list) {
  document.querySelector('#answer').innerHTML+=`<li>${name}</li>`;
}
