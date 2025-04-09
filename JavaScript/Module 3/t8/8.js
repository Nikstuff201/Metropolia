'use strict';


function calculate(evt) {
  const num1 = parseInt(document.querySelector('#num1').value);
  const num2 = parseInt(document.querySelector('#num2').value);
  const choice = document.querySelector('#operation').value;

  let result
  if (choice === 'add') {
    result = num1 + num2;
  } else if (choice === 'sub') {
    result = num1 - num2;
  } else if (choice === 'multi') {
    result = num1 * num2;
  } else {
    result = num1 / num2;
  }

  document.querySelector('#result').innerHTML = `${result}`;
}

document.querySelector('#start').addEventListener('click',calculate)
