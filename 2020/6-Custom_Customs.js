const getInput = require('./get-input');

async function getGroups() {
    const input = await getInput(6);
    return input.trim().split(/\n\s/g).map(g => g.split(/\n/g));
}

function getQuestionCount1(group) {
    let q = 0;
    const set = new Set();
    let totalString = group.join('');
    for(let char of totalString) {
        if (!set.has(char)) {
            q++;
            set.add(char);
        }
    }

    return q;
}

function getQuestionCount2(group) {
    let q = 0;
    const map = {};
    
    group.forEach(person => {

        for (let ans of person) {
            if (!map[ans]) map[ans] = 0;
            map[ans]++;
        }
    });

    for (let key in map) {
        if (map[key] === group.length) q++;
    }

    return q;
}

async function main() {
    const groups = await getGroups();

    let total = 0;

    groups.forEach(g => total += getQuestionCount2(g));

    console.log(total);
}

main();