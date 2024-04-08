#!/usr/bin/node
// script that prints x times “C is fun”

const args = process.argv.slice(2);
const language = 'C is fun';

if (isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[0]; i++) { console.log(language); }
}
