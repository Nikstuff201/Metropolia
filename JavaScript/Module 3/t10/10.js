'use strict';

function name(evt){
  evt.preventDefault();
  const form=document.querySelector('#source');
  const name=form.elements.firstname.value;
  const surname=form.elements.lastname.value;
  const result=`Your name is ${name} ${surname}`;
  document.querySelector('#target').innerHTML=result;
}

const button=document.querySelector('input[type="submit"]');
button.addEventListener('click', name);

