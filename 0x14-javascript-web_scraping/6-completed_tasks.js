#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (!error) {
    const tasks = JSON.parse(body);

    const usersCompletedTask = {};
    tasks.forEach((todo) => {
      if (todo.completed) {
        if (usersCompletedTask[todo.userId]) { usersCompletedTask[todo.userId] += 1; } else { usersCompletedTask[todo.userId] = 1; }
      }
    });
    console.log(usersCompletedTask);
  }
});
