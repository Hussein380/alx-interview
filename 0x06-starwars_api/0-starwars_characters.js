#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];

// Base URL for the Star Wars API
const baseUrl = 'https://swapi.dev/api/films/';

// Function to fetch movie details
function fetchMovieCharacters(movieId, callback) {
  const url = `${baseUrl}${movieId}/`;

  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    if (response.statusCode === 200) {
      callback(body.characters); // Pass the character URLs to the callback
    } else {
      console.error('Failed to fetch movie data:', response.statusCode);
    }
  });
}

// Function to fetch character names from their URLs
function fetchCharacterNames(characterUrls, callback) {
  let characters = [];
  let count = 0;

  // Function to handle individual character requests
  function fetchNext() {
    if (count >= characterUrls.length) {
      return callback(characters);
    }

    request(characterUrls[count], { json: true }, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
      } else if (response.statusCode === 200) {
        characters.push(body.name); // Collect character names
      } else {
        console.error('Failed to fetch character data:', response.statusCode);
      }
      count++;
      fetchNext(); // Fetch the next character
    });
  }

  fetchNext(); // Start fetching characters
}

// Main function to fetch and display characters
function displayCharacters() {
  fetchMovieCharacters(movieId, (characterUrls) => {
    fetchCharacterNames(characterUrls, (names) => {
      names.forEach(name => console.log(name)); // Print each character name
    });
  });
}

// Call the main function
displayCharacters();

