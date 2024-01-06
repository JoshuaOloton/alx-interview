#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.hbtn.io/api';
const filmId = process.argv[2];

if (process.argv.length > 2) {
  request(`${BASE_URL}/films/${filmId}/`, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const charactersArray = JSON.parse(body).characters;
    const charactersName = charactersArray.map(
      character => new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
