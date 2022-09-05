#!/usr/bin/node

const squareSize = process.argv[2];

for (let width = 0; width < squareSize; width++) {
  let side = '';
  for (let height = 0; height < squareSize; height++) {
    side += 'X';    
  }
  console.log(side);
}
