'use strict';

function even(list) {
  const uuslist=[];
  for (let number of list) {
    if (number%2===0) {
      uuslist.push(number);
    }
  }
  return uuslist;
}

const list= [2,3,4,5,9,4,7,6,5];

const uuslist=even(list);

console.log(list);
console.log(uuslist);

