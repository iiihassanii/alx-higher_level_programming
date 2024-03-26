#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];
const string = process.argv[3];

fs.open(fileName, 'a', function (fd) {
  fs.write(fd, string, function () {
  });
});
