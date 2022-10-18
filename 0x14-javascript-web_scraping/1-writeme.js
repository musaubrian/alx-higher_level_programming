#!/usr/bin/node

// reads and writes content to a file
// passed as an arguments

const fs = require('fs');
const file = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(file, contentToWrite, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
