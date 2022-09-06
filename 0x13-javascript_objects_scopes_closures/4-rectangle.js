#!/usr/bin/node

// class defining a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Rectangle();
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let index = 0; index < this.height; index++) {
      let rectView = '';
      for (let index = 0; index < this.width; index++) {
        rectView += 'X';        
      }
      console.log(rectView);      
    }
  }

  rotate() {
    const newHeight = this.width;
    const newWidth = this.height;
    this.height = newHeight;
    this.width = newWidth;
  }
  
  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
