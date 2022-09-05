#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let width = 0; width < squareSize; width++) {
    let side = '';
    for (let height = 0; height < squareSize; height++) {
      side += 'X';      
    }
    console.log(side);
  }
}
