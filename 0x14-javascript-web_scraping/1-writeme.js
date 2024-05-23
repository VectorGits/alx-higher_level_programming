#!/usr/bin/node
// Write to file

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
    }
  });
