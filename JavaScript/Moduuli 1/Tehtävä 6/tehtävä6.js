'use strict';
let result;
const answer=confirm('Should I calculate a square root?');
if (answer==true) {
  const number=parseFloat(prompt('Give your number'));
  if (number>=0) {
    result=Math.sqrt(number);
  }
  else {
    result=`${number} square root cannot be found`;
  }
}
else {
  result='The square root is not calculated';
}
document.querySelector("#vastaus").innerHTML=`${result}`;