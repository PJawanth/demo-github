const assert = require('assert');
const { execSync } = require('child_process');

const output = execSync('node index.js', { encoding: 'utf8' }).trim();
assert.strictEqual(output, 'Hello, world!');
console.log('Test passed');
