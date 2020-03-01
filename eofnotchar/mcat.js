/* mcat.js */
const fs = require('fs');
const process = require('process');

const fileName = process.argv[2];

var readable = fs.createReadStream(fileName, {
  encoding: 'utf8',
  fd: null,
});

readable.on('readable', function() {
  var chunk;
  while ((chunk = readable.read(1)) !== null) {
    process.stdout.write(chunk); /* chunk is one byte */
  }
});

readable.on('end', () => {
  console.log('\nEOF: There will be no more data.');
});
