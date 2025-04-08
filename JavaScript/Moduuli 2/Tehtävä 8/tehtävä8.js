'use strict';


function conсat(list) {
  let result=''
  for (let name of list) {
    result+=name;
  }
  return result;
}

const list=['Jonni','Anna','Nikita','Kolya'];

const output=conсat(list);

document.querySelector('#answer').innerHTML=`${output}`;