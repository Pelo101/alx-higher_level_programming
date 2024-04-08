#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const nums = process.argv.slice(2).map(Number).filter(num => !isNaN(num));
const secondLgst = nums.sort((a, b) => b - a)[1] || 0;

console.log(secondLgst);
