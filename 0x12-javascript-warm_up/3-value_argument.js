#!/usr/bin/node
//  script that prints the first argument passed to it

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No arguments');
} else if (!args[1]);
{
  console.log(args[0]);
}
