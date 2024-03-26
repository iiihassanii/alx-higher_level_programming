#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + episode, function (error, response, body) {
  if (!error) {
    const movie = JSON.parse(body);
    console.log('Title:', movie.title);
  }
});
