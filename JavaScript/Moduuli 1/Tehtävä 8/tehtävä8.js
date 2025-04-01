'use strict';
let year1, year2;
year1=parseInt(prompt('Give your first year'));
year2=parseInt(prompt('Give your last year'));
while (!((year1 % 4 == 0 && year1 % 100 != 0) || (year1 % 4 == 0 && year1 % 100 == 0 && year1 % 400 == 0))){
  year1++;
}
while (!((year2 % 4 == 0 && year2 % 100 != 0) || (year2 % 4 == 0 && year2 % 100 == 0 && year2 % 400 == 0))){
  year2--;
}

for (;year1<=year2;year1+=4) {
  if ((year1 % 4 == 0 && year1 % 100 != 0) || (year1 % 4 == 0 && year1 % 100 == 0 && year1 % 400 == 0)){
    document.querySelector('#year').innerHTML+=`<li>${year1}</li>`;
  }
}