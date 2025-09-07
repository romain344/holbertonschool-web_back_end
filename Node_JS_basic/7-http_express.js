const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line !== '');
      lines.shift(); // retirer l’en-tête

      const students = {};
      let total = 0;

      for (const line of lines) {
        const parts = line.split(',');
        if (parts.length >= 4) {
          total += 1;
          const firstname = parts[0].trim();
          const field = parts[3].trim();

          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
        }
      }

      let output = `Number of students: ${total}\n`;
      for (const [field, list] of Object.entries(students)) {
        output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  countStudents(database)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(1245);

module.exports = app;