#!/usr/bin/node
// script that imports an array and computes a new array.

const { list } = require('./100-data.js');

const list1 = list.map((x, i) => x * i);

console.log(list);
console.log(list1);
