#!/usr/bin/node
/*
 * a script that prints My number: <first argument converted in integer>
 */
const argv = process.argv;

const myVar = parseInt(argv[2]);
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myVar}`);
}
