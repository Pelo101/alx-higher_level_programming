#!/usr/bin/node
// a script that prints a square

const args = process.argv.slice(2);
const SquareCharacter = 'X';

if (isNaN(args[0])) {
  console.log('Misssing size');
} else {
  const SquareSize = parseInt(args[0]);
  let line = '';

  for (let i = 0; i < SquareSize; i++) {
    line += SquareCharacter;
  }
  for (let j = 0; j < SquareSize; j++) {
    console.log(line);
  }
}
