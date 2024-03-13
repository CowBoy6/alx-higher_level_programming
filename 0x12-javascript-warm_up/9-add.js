#!/usr/bin/node
function add (a, b) {
  console.log(Number(b) + Number(a));
}
add(process.argv[2], process.argv[3]);
