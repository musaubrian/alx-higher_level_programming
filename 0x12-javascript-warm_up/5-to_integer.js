#!/usr/bin/node

const numToParse = parseInt(process.argv[2]);

if (isNaN(numToParse)) {
  console.log('Not a number');
} else {
  console.log(numToParse);
}
