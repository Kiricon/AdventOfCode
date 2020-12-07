const getInput = require('./get-input');

async function getPasswords() {
    const input = await getInput(2);
    return input.trim().split(/\n/g).map(line => {
        if (!line.length) return null;
        let split = line.split(' ');
        //console.log(split);
        return {
            charCount: split[0].split('-').map(c => parseInt(c)),
            char: split[1][0],
            text: split[2]
        }
    });
}

function isValidPassword1({ charCount, char, text }) {
    let seenCount = 0;
    for (let c of text) {
        if (c === char) seenCount++;
        if (seenCount > charCount[1]) return false;
    }

    return seenCount >= charCount[0] && seenCount <= charCount[1];
}

function isValidPassword2({ charCount, char, text }) {
    return (text[charCount[0]-1] === char) !== (text[charCount[1]-1] === char)
}

async function main() {
    const passwords = await getPasswords();

    let validCount = 0;

    passwords.forEach(p => {
        if (isValidPassword2(p)) validCount++;
    });

    console.log(validCount);
}

main();
