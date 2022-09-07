#!/usr/bin/node

// converts from base 10 to base passed as argument

exports.converter = function (base) {
  return function (toConv) {
    return toConv.toString(base)
  }
}
