'use strict';
const name=prompt('Give your name');
const number=Math.floor(Math.random()*4)+1;
let place
if (number==1) {
  place='Gryffindor';
} else if (number==2) {
  place='Slytherin';
} else if (number==3) {
  place='Hufflepuff';
} else {
  place='Ravenclaw'
}
document.querySelector('#kutsu').innerHTML=`${name} you are in ${place}́.`

