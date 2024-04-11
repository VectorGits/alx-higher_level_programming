#!/usr/bin/node

// Get all args
const args = process.argv.slice(2);

// Check if first arg exists and prints the first arg
if (args[0] !== undefined) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
