'use strict';
const names = ['John', 'Paul', 'Jones'];
for (let name of names) {
  document.querySelector('#target').innerHTML += `<li>${name}</li>`;
}
