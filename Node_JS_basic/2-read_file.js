module.exports = function countStudents(path) {
    const fs = require('fs');
    let data;
    try {
        data = fs.readFileSync(path, 'utf8');
    } catch (err) {
        throw new Error('Cannot load the database');
    }

    const lines = data.split('\n').filter(line => line.trim() !== '');
    const students = lines.slice(1);
    console.log(`Number of students: ${students.length}`);
    const fields = {};

    students.forEach(student => {
        const parts = student.split(',');
        const name = parts[0].trim();
        const field = parts[3].trim();

        if (!fields[field]) {
            fields[field] = [];
        }
        fields[field].push(name);
    });
    for (const field of Object.keys(fields)) {
        const listNames = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${listNames}`);
    }
}