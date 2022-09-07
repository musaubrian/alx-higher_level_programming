#!/usr/bin/node

// class defining a square
// inheriting from a rectangle

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let squareView = '';
      for (let j = 0; j < this.size; j++) {
        squareView += c;
      }
      console.log(squareView);
    }
  }
};
