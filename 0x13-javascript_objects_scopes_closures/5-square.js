#!/usr/bin/node
/*
 * an empty class Square that inherits from rectangle
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (s) {
    super(s, s);
    this.size = this.width;
  }
}
module.exports = Square;
