#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”

const args = process.argv.slice(2);

if (args.length >= 2) {
  console.log(`${argv[0]} is ${argv[1]}`);
}
