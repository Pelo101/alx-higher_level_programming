#!/usr/bin/node

require('request')(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (_err, _res, body) => console.log(JSON.parse(body).title)
);
