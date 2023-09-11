#!/usr/bin/node
/*
 * a script that prints x times "C is fun"
 */
const argv = process.argv;
const myVar = parseInt(argv[2]);
if (isNaN(myVar)) {
  console.log('Missing number of occurrence');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
