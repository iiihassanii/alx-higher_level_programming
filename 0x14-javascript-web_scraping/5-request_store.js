#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (!error) {
    fs.open(fileName, 'a', function (err, fd) {
      if (err) { console.log(err); } else {
        fs.write(fd, body, 'utf8', function (err) {
          if (err) { console.log(err); }
        });
      }
    });
  }
});
