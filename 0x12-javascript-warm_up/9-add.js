#!/usr/bin/node

const numOne = parseInt(process.argv[2]);
const numTwo = parseInt(process.argv[3]);

function add(a, b) {
  return a + b;
}
console.log(add(numOne, numTwo));
