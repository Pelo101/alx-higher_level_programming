#!/usr/bin/node
//  script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

const args = process.argv.slice(2);

if (isNaN(args)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${args}`);
}
