#!/usr/bin/node
/*
 * a script that prints x times "C is fun"
 */
const argv = process.argv;
const myVar = parseInt(argv[2]);
let str = '';
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    for (let j = 0; j < myVar; j++) {
      str += 'X';
    }
    if (i !== myVar - 1) {
      str += '\n';
    }
  }
  console.log(str);
}
