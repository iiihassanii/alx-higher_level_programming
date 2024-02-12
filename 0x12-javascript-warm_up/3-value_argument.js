#!/usr/bin/node
if (process.argv.length <= 2) { console.log('No argument'); } else {
  process.argv.slice(2).forEach(arg => {
    console.log(`${arg}`);
  });
}
