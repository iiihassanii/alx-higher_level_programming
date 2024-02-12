#!/usr/bin/node
const len = process.argv.length;
let max, min;
if (len <= 3) {
  console.log(0);
} else {
  min = 2;
  max = 2;
  for (let i = 2; i < len; i++) {
    if (Number(process.argv[i]) > Number(process.argv[max])) {
      min = max;
      max = i;
    } else if (Number(process.argv[i]) > process.argv[min]) { min = i; }
  }
  console.log(process.argv[min]);
}
