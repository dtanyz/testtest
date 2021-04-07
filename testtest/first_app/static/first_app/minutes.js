const addRowButton = document.getElementById("add-new-row")
const deleteRowButtons = document.getElementsByClassName("delete-row")
const minutesTable = document.getElementById("minutes-table");
let rowNumber = 0


addRowButton.addEventListener('click', function() {    
    rowNumber ++

    const row = minutesTable.insertRow(-1);
    const cell1 = row.insertCell(0);
    const cell2 = row.insertCell(1);


    cell1.setAttribute("style", "vertical-align: top;");

    cell1.innerHTML = `<input class="form-control" type='text' id='speaker${rowNumber}' name='speaker' placeholder='Speaker'><br><button style="padding:0;" type="button" class="btn btn-warning mr-auto delete-row" id="delete-row${rowNumber}" onclick="deleteRow(this)">Delete Row</button>`;
    cell2.innerHTML = `<textarea class="form-control" id="write_up${rowNumber}" name="write_up" rows="4" cols="50" 
      // placeholder="Message"></textarea>`;
});

function deleteRow(btn) {
  const row = btn.parentNode.parentNode;
  row.parentNode.removeChild(row);
}

const dutyInstructor = document.getElementById("duty_instructor");
const minutesTaker = document.getElementById("minutes_taker");
const dateEntry = document.getElementById("datepicker");

const form = document.getElementsByTagName("form")[0];
const diError = document.getElementById("di_error");
const takerError = document.getElementById("taker_error");
const dateError = document.getElementById("date_error");

form.addEventListener('submit', function(e) {
    if (dutyInstructor.value === "Choose...") {
        e.preventDefault();
        diError.innerHTML = '<p style="color:red;"><small>Choose a Duty Instructor</small></p>';
        $('#toSubmit').modal('hide');
    } else {
      diError.innerHTML = '';
    };

    if (minutesTaker.value === "Choose...") {
        e.preventDefault();
        takerError.innerHTML = '<p style="color:red;"><small>Choose a Minutes Taker</small></p>';
        $('#toSubmit').modal('hide');
    } else {
        takerError.innerHTML = '';
    };

    var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
    let wrongFormat = false

    if (dateEntry.value.match(dateformat)) {
      var opera1 = dateEntry.value.split('/');
      var opera2 = dateEntry.value.split('-');
      lopera1 = opera1.length;
      lopera2 = opera2.length;

      if (lopera1>1) var pdate = dateEntry.value.split('/');
      else if (lopera2>1) var pdate = dateEntry.value.split('-');

      var dd = parseInt(pdate[0]);
      var mm  = parseInt(pdate[1]);
      var yy = parseInt(pdate[2]);

      var ListofDays = [31,28,31,30,31,30,31,31,30,31,30,31];

      if (mm==1 || mm>2) {
        if (dd>ListofDays[mm-1]) wrongFormat = true;
      }
      if (mm==2) {
        var lyear = false;
        if ( (!(yy % 4) && yy % 100) || !(yy % 400)) {
          lyear = true;
        }
        if ((lyear==false) && (dd>=29)) wrongFormat = true;
        if ((lyear==true) && (dd>29)) wrongFormat = true;
      }
    } else {
      wrongFormat = true
    }

    if (wrongFormat) {
      e.preventDefault();
      dateError.innerHTML = '<p style="color:red;"><small>Invalid date format. Date format must be in dd/mm/yyyy.</small></p>';
      $('#toSubmit').modal('hide');
    } else {
      dateError.innerHTML = ''
    }
});
