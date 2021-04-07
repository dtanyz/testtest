for (ans in answers) {
    if (ans === "bf_user") break;
    else if (answers[ans]) {
        document.getElementById(`${ans}`).value = `${answers[ans]}`;
    } else {
        document.getElementById(`${ans}`).className += ' wrong';
    }
}