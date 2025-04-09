'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const element=document.querySelector('#target')
for (let object of students){
  let option=document.createElement('option')
  option.value=object.id
  option.textContent=object.name
  element.appendChild(option)
}

