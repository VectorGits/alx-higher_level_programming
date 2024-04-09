#!/usr/bin/node


// Get first arg
const arg = process.argv.slice(2);

// Conversion to an Integer
const num = parseInt(arg);

// Check if the result is a number and print the appropriate message
if (isNaN(num)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + num);
}