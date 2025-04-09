'use strict';

function click(evt) {
  alert(evt.currentTarget.tagName + ' was clicked');
}



const button=document.querySelector('button');
button.addEventListener('click',click);


