#!/usr/bin/node
// function that increment and calls a function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  return theFunction(number);
};
