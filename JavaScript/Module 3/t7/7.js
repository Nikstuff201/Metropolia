'use strict';

const target=document.querySelector('#target');
const trigger=document.querySelector('#trigger');
trigger.style.display='inline';

function hovup(evt) {
  target.src='img/picB.jpg';
}

function hovdown(evt){
  target.src='img/picA.jpg';
}

trigger.addEventListener('mouseenter', hovup);
trigger.addEventListener('mouseleave',hovdown);