#!/usr/bin/node
// Include fs module
const fs = require('fs');

const fileName = process.argv[2];
fs.readFile(fileName, 'utf8', function (err, data) {
  if (data !== undefined) { console.log(data); } else { console.log(err); }
});
