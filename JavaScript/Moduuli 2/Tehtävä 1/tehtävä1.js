'use strict'
const numbers=[]
let number
for (let i=0; i<=4; i++) {
  numbers[i]=parseInt(prompt(`Give you number ${i+1}`))
}

for (let i=4; i>=0; i--) {
  document.querySelector('#numbers').innerHTML+=`${numbers[i]}<br>`
}
