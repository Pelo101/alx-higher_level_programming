#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const todo = JSON.parse(body);
  const userTasks = {};

  todo.forEach(todos => {
    if (todos.completed) {
      userTasks[todos.userId] = (userTasks[todos.userId] || 0) + 1;
    }
  });

  for (const [userId, count] of Object.entries(userTasks)) {
    console.log(`User ${userId} has completed ${count} tasks`);
  }
});
