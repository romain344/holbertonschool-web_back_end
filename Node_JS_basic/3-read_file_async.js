const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n').filter((line) => line !== '');
      lines.shift(); // enlever l’en-tête

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

      console.log(`Number of students: ${total}`);
      for (const [field, list] of Object.entries(students)) {
        console.log(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;