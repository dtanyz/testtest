var value = JSON.parse(document.getElementById('boldface-data').textContent); 

const test = JSON.parse(value)[0];

const answers = test.fields;

for (ans in answers) {
    if (ans === "bf_user") break;
    else if (answers[ans]) {
        document.getElementById(`${ans}`).value = `${answers[ans]}`;
        // document.getElementById(`${ans}`).disabled = true;
    } 
}