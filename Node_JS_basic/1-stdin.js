    console.log('Welcome to Holberton School, what is your name?');
    process.stdin.on('data', function (data) {
        console.log('Your name is: ' + data.toString().trim());
    });
    process.stdin.on('end', function () {
        console.log('This important software is now closing');
    });