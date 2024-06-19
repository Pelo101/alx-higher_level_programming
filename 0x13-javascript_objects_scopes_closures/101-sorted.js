#!/usr/bin/node
// a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data.js');

const ndict = Object.entries(dict).reduce((acc, [key, value]) => {
  if (!acc[value]) {
    acc[value] = [];
  }
  acc[value].push(key);
  return acc;
}, {});
console.log(ndict);
