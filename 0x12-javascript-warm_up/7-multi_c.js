#!/usr/bin/node

const numOfTimes = parseInt(process.argv[2]);

if (isNaN(numOfTimes)) {
  console.log('MIssing number of occurences');
} else {
  for (let index = 0; index < numOfTimes; index++) {
    console.log('C is fun');
  }
}
