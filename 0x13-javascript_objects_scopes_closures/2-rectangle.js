#!/usr/bin/node
/*
 * an empty class Rectangle that defines a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
