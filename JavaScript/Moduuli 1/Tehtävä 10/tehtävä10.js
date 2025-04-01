'use strict';
const dice=parseInt(prompt('Give number of dices'));
const summa=parseInt(prompt('Give the summ of dices'));
let part=0;
for (let i=1; i<=10000; i++) {
  let number=0;
  for (let dices=1; dices<=dice; dices++){
    number+=Math.floor(Math.random()*6+1);
  }
  if (number===summa){
    part+=1;
  }
}

let result=(part/10000*100).toFixed(4);

document.querySelector('#probability').innerHTML=`Probability to get sum ${summa} of ${dice} dice is ${result}%`