#!/usr/bin/node
let A = [];
A = process.argv;
if (A[2]) {
  console.log(A[2]);
} else if (!A[2]) { console.log('No argument'); }
