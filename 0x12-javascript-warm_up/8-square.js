#!/usr/bin/node
// a script that prints a square

const args = process.argv.slice(2);
const SquareCharacter = 'X';

if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  const SquareSize = parseInt(args[0]);

  for (let i = 0; i < SquareSize; i++) {
    let line = '';

    for (let j = 0; j < SquareSize; j++) {
      line += SquareCharacter;
    }

    console.log(line);
  }
}
