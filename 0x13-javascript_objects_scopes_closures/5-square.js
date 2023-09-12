#!/usr/bin/node
/*
 * an empty class Square that inherits from rectangle
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
