#!/usr/bin/node
let A = [];
A = process.argv;
if (A.length === 2) {
  console.log('No argument');
} else if (A.length > 2) { console.log('Arguments found'); }
