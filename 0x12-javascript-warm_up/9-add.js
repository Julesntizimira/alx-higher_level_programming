#!/usr/bin/node
/*
 * a script that prints the addition of 2 integers
 */
const argv = process.argv;
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(argv[2]), parseInt(argv[3])));
