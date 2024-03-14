#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < parseInt(list.length / 2); i++) {
    let temp = 0;
    temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }
  return list;
};
