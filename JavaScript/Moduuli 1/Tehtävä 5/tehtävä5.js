'use strict';
const year=parseInt(prompt('Anna vuosi'))
let answer
if (year%4==0) {
  if (year%100==0){
    if (year%400==0){
      answer=`${year} is a leap year`;
    }
    else {
      answer=`${year} not a leap year!`;
    }
  }
  else {
    answer=`${year} is a leap year`
  }
}
else {
  answer=`${year} not a leap year`
}
document.querySelector('#answer').innerHTML=answer
