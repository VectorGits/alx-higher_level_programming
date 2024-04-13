#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
  process.exit(0);
}

args.sort((a, b) => b - a);

for (let x = 0; x < args.length; x++) {
  if (args[x] < args[0]) {
    console.log(args[x]);
    process.exit(0);
  }
}

console.log(0);
