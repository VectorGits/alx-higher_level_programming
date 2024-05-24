#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
