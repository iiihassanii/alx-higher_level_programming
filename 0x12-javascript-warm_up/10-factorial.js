#!/usr/bin/node
function Factorial (number) {
  if (number === 0 || isNaN(number)) {
    return (1);
  }
  return (number * Factorial(number - 1));
}

console.log(Factorial(Number(process.argv[2])));
