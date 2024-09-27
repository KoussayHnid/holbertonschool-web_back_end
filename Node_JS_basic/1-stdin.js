process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  // const name = data.toString().trim();
  const name = process.stdin.read();
  if (name) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

process.stdin.on('close', () => {
  process.stdout.write('This important software is now closing\n');
});
