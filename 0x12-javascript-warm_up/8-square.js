#!/usr/bin/node
if (isNaN(process.argv[2])) { console.log('Missing size'); } else {
  for (let i = 0; i < process.argv[2]; i++) {
    let row = '';
    for (let j = 0; j < process.argv[2]; j++) { row += 'X'; }
    console.log(row);
  }
}
