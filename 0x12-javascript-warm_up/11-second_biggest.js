#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myArr = process.argv.slice(2);
  myArr.sort((a, b) => b - a);
  console.log(myArr[1]);
}
