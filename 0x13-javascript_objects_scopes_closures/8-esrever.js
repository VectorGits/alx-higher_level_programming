#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let x = 0; x < list.length; x++) {
    reversedList.unshift(list[x]);
  }
  return reversedList;
};
