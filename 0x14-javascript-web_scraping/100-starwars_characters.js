#!/usr/bin/node
// prints all characters of a Star Wars movie ID

const request = require('request');
const movieID = process.argv[2];
const apiURL = `https://swapi-api.hbtn.io/api/films/${movieID}`;

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  for (const characterUrl of charactersUrls) {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
