---

# Star Wars Characters Script

This project provides a Node.js script to fetch and display the names of characters from a specified Star Wars movie using the Star Wars API. The script uses the `request` module to make HTTP requests and handle asynchronous operations.

## Getting Started

### Prerequisites

- Node.js (version 10.x or higher)
- `request` module
- `semi-standard` for code style (optional for linting)

### Installation

1. **Install Node.js** if not already installed:

   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install the `request` module** globally:

   ```bash
   sudo npm install request --global
   ```

3. **Install `semi-standard` globally** (for code style):

   ```bash
   sudo npm install semistandard --global
   ```

### Usage

1. **Create the script file** named `0-starwars_characters.js`:

   ```javascript
   #!/usr/bin/node

   const request = require('request');

   const movieId = process.argv[2];

   const baseUrl = 'https://swapi.dev/api/films/';

   function fetchMovieCharacters(movieId, callback) {
     const url = `${baseUrl}${movieId}/`;

     request(url, { json: true }, (error, response, body) => {
       if (error) {
         console.error('Error fetching movie data:', error);
         return;
       }

       if (response.statusCode === 200) {
         callback(body.characters);
       } else {
         console.error('Failed to fetch movie data:', response.statusCode);
       }
     });
   }

   function fetchCharacterNames(characterUrls, callback) {
     let characters = [];
     let count = 0;

     function fetchNext() {
       if (count >= characterUrls.length) {
         return callback(characters);
       }

       request(characterUrls[count], { json: true }, (error, response, body) => {
         if (error) {
           console.error('Error fetching character data:', error);
         } else if (response.statusCode === 200) {
           characters.push(body.name);
         } else {
           console.error('Failed to fetch character data:', response.statusCode);
         }
         count++;
         fetchNext();
       });
     }

     fetchNext();
   }

   function displayCharacters() {
     fetchMovieCharacters(movieId, (characterUrls) => {
       fetchCharacterNames(characterUrls, (names) => {
         names.forEach(name => console.log(name));
       });
     });
   }

   displayCharacters();
   ```

2. **Make the script executable**:

   ```bash
   chmod +x 0-starwars_characters.js
   ```

3. **Run the script** with the Movie ID as an argument:

   ```bash
   ./0-starwars_characters.js 3
   ```

   Replace `3` with the desired movie ID to get characters for that movie.

### Example

To get the list of characters for "Return of the Jedi" (Movie ID 3), run:

```bash
./0-starwars_characters.js 3
```

The script will print each character's name on a new line.

### Additional Information

- **API Used**: [Star Wars API (SWAPI)](https://swapi.dev/)
- **Script**: Fetches character names from the movie based on the provided Movie ID and displays them in order.

### Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

