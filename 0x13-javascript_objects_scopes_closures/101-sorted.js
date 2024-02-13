#!/usr/bin/node

const { dict } = require('./101-data');

const usrOccDict = {};

for (const userId in dict) {
  const occ = dict[userId];
  if (usrOccDict[occ] === undefined) {
    usrOccDict[occ] = [];
  }
  usrOccDict[occ].push(userId);
}

console.log('User IDs by Occurrence:', usrOccDict);
