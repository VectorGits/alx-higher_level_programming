#!/usr/bin/node
// Write arg to file overwrite if exists

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
    }
  });
