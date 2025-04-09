'use strict';

function calculate(evt) {
  function strtoint(list){
    for (let i in list){
      list[i]=parseInt(list[i]);
    }
  }
  const input=document.querySelector('#calculation').value;
  let result;

  if (input.includes('+')) {
    const numbers = input.split('+');
    strtoint(numbers);
    result = numbers[0];
    for (let i of numbers.slice(1)) {
      result += i;
    }
  }

  else if (input.includes('-')) {
    const numbers=input.split('-');
    strtoint(numbers);
    result=numbers[0];
    for (let i of numbers.slice(1)) {
      result-=i;
    }
  }

  else if (input.includes('*')) {
    const numbers = input.split('*');
    strtoint(numbers);
    result = numbers[0];
    for (let i of numbers.slice(1)) {
      result = result * i;
    }
  }

  else if (input.includes('/')) {
    const numbers = input.split('/');
    strtoint(numbers);
    result = numbers[0];
    for (let i of numbers.slice(1)) {
      result = result/i;
    }
  }
  document.querySelector('#result').innerHTML=`${result}`;
  }

document.querySelector('#start').addEventListener('click',calculate);
