'use strict';
let number1,number2,number3
number1=parseInt(prompt('Anna numero 1'))
number2=parseInt(prompt('Anna numero 2'))
number3=parseInt(prompt('Anna numero 3'))
document.querySelector('#summa').innerHTML=`Summa on ${number1+number2+number3}`
document.querySelector('#kerto').innerHTML=`Kerto on ${number1*number2*number3}`
document.querySelector('#keskiarvo').innerHTML=`Keskiarvo on ${(number1*number2*number3)/3}`
