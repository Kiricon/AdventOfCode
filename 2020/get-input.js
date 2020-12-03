const fetch = require('node-fetch');
async function getInput(day) {
    return (await fetch(`https://adventofcode.com/2020/day/${day}/input`, {
        headers: {
            'Cookie': 'session=53616c7465645f5fcd57dc0807dc48eb9eb46888d2a600d83268d38558910a7f1fb6178cb4728a5885388f73b24c0451'
        }
    })).text();
}

module.exports = getInput;