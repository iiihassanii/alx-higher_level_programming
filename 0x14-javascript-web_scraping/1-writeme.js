#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];
const string = process.argv[3];

fs.open(fileName, 'a', function (err, fd) {
  if (err) { console.log(err); } else {
    fs.write(fd, string, 'utf8', function (err) {
      if (err) { console.log(err); }
    });
  }
});
