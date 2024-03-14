#!/usr/bin/node
module.exports = function nbOccurences (A, n) {
  let occurence = 0;
  for (let i = 0; i < A.length; i++) { if (A[i] === n) { occurence++; } }
  return occurence;
};
