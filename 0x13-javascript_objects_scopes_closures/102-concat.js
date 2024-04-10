#!/usr/bin/node

const fs = require('fs');
const path = require('path');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(path.join(__dirname, fileA), 'utf-8');
const contentB = fs.readFileSync(path.join(__dirname, fileB), 'utf-8');

fs.writeFileSync(path.join(__dirname, fileC), contentA + contentB);
