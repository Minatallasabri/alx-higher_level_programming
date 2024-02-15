#!/usr/bin/node
let funny = 0;

exports.logMe = function (item) {
  console.log(funny + ': ' + item);
  funny++;
};
