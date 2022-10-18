#!/usr/bin/node

// prints the title of a Star Wars movie 
// where the episode number matches a given integer.

const request = require('request');
const episodeNumber = process.argv[2];
const apiUrl = "https://swapi-api.hbtn.io/api/films/";

request(apiUrl + episodeNumber, function (error, response, body) {
    if (error) {
        throw error;
    } else if (response.statusCode === 200) {
        const jsonResponse = JSON.parse(body);
        console.log(jsonResponse.title);
    } else {
        console.log('Error code: ' + response.statusCode);
    }
})
