#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', res.statusCode);
});
