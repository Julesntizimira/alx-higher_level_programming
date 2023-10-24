#!/usr/bin/node
/*
 * a script that prints the number of movies
 * where the character Wedge Antilles is present.
 */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const newObj = JSON.parse(body);
    console.log(newObj.films.length);
  }
});
