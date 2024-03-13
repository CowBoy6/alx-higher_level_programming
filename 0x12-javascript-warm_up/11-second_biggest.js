#!/usr/bin/node
if (process.argv[2] === 0 || process.argv[2] === 1) { console.log('1'); } else {
  let A = [];
  let k = 0;
  for (let i = 2; i < process.argv.length; i++) {
    A[k] = process.argv[i];
    k++;
  }
  A = A.sort(function (a, b) { return b - a; });
  console.log(A[1]);
}
