#!/usr/bin/node

// class defining a square
// inheriting from a rectangle

const square = require('./5-square');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let squareView = '';
      for (let i = 0; i < this.size; i++) {
        squareView += c;
      }
      console.log(squareView);
    }
  }
};
