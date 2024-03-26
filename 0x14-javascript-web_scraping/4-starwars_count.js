#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = '18';
request(url, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    let count = 0;

    for (const movie of movies) {
      for (const character of movie.characters) {
        if (character.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
