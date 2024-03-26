#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = '18';
request(url, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    let count = 0;

    movies.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
