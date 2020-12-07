const getInput = require('./get-input');

async function getPassports() {
    const input = await getInput(4);
    return input.split(/\n\s/g).map(line => line.split(/\n|\s/g)).map(keyVals => {
        let obj = {};
        keyVals.forEach(keyVal => {
            let split = keyVal.split(':');
            obj[split[0]] = split[1];
        })

        return obj;
    });
}

const eyeSet = new Set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']);

function isValid({byr, iyr, eyr, hgt, hcl, ecl, pid, cid}) {
    if (!(byr && iyr && eyr && hgt && hcl && ecl && pid)) return false;
    

    byr = parseInt(byr);
    iyr = parseInt(iyr);
    eyr = parseInt(eyr);
    
    if (byr < 1920 || byr > 2002) return false;
    if (iyr < 2010 || iyr > 2020) return false;
    if (eyr < 2020 || eyr > 2030) return false;

    

    const hgtCM = hgt.split('cm');
    const hgtIN = hgt.split('in');
    if (hgtCM.length > 1) {
        if (hgtCM[0] < 150 || hgtCM[0] > 193) return false;
    } else if (hgtIN.length > 1) {
        if (hgtIN[0] < 59 || hgtIN[0] > 76) return false;
    } else {
        return false;
    }

    if (hcl[0] !== '#') return false;
    if (hcl.split('#')[1].length !== 6) return false;
    if (!/^[a-z0-9]+$/i.test(hcl.split('#')[1])) return false;
    
    if (!eyeSet.has(ecl)) return false;
    
    if (pid.length !== 9) return false;
    if (isNaN(pid)) return false;

    

    return true;
}

async function main() {
    const passports = await getPassports();

    let validCount = 0;

    passports.forEach(p => {
        if (isValid(p)) validCount++
    });

    console.log(validCount);
}

main();