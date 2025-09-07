const http = require('http');
const fs = require('fs');

const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line !== '');
      lines.shift(); // enlever l’entête

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

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');
    countStudents(database)
      .then((output) => {
        res.end(output);
      })
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;