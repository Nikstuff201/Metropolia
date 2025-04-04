'use strict';

const noc=parseInt(prompt('Give the number of candidates'));
const loc=[];


let name;

for (let i=1; i<=noc; i++) {
  const nof=prompt(`Give the name on candidate ${i}`);
  const candidate={
    name: nof,
    votes: 0,
  }
  loc.push(candidate);
}

const nov=parseInt(prompt('Give the  number of vouters'));

for (let i=1;i<=nov;i++) {
  const vote=prompt('Give the name of your candidate');
  if (vote !=='') {
    for (let i of loc) {
      if (i.name===vote){
        i.votes++;
      }
    }
  }
}



loc.sort((a,b)=>b.votes-a.votes);

console.log(`The winner is ${loc[0].name} with ${loc[0].votes} votes`);
console.log('results:')
for (let i of loc) {
  console.log(`${i.name}: ${i.votes} votes`);
}




