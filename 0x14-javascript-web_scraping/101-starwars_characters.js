#!/usr/bin/node
// Retrieve and print all Star Wars character names from a movie ID

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

  function printCharacterName (index) {
    if (index < charactersUrls.length) {
      request(charactersUrls[index], (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        const character = JSON.parse(body);
        console.log(character.name);

        printCharacterName(index + 1);
      });
    }
  }

  printCharacterName(0);
});
