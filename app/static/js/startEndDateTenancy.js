//Code adapted from source https://codepen.io/luv2code/pen/oNvrWyZ

// Create default date
let date = new Date();

// SET OPTIONS FOR #start_date
let optionsStartDate = {
    autoClose: true,
    showClearBtn: true,
    format: 'dd mmmm yyyy',
    onSelect: function(selectedDate) {
        const selectedDateObj = new Date(selectedDate);

        const getMonth = selectedDateObj.getMonth()+1;
        console.log("getMonth get month " + getMonth)

        const setMonth = new Date(selectedDateObj.setMonth(getMonth))
        console.log("setMonth " + setMonth)

        setMinEndDate(setMonth);
    }
};


// SET OPTIONS FOR #end_date
let optionsEndDate = {
    autoClose: true,
    showClearBtn: true,
    format: 'dd mmmm yyyy',
};


//INITIATE DATEPICKER
document.addEventListener('DOMContentLoaded', function () {
    let startDate = document.querySelector('#start_date');
    let instanceStart = M.Datepicker.init(startDate, optionsStartDate);

    let endDate = document.querySelector('#end_date');
    let instanceEnd = M.Datepicker.init(endDate, optionsEndDate);
});


// FUNCTION TO SET MINIMUM DATE WHEN #start_date DATE SELECTED
var setMinEndDate = function(MinEndDate) {
    // Get the current date set on #end_date datepicker
    let selectedEndDate = M.Datepicker.getInstance(document.querySelector('#end_date'));
    selectedEndDate.options.minDate = MinEndDate;

    // Check if the #start_date date is greater than the #end_date date and modify by 1 day if true.
    if (new Date(selectedEndDate) < MinEndDate) {
        selectedEndDate.setDate(MinEndDate);
        document.querySelector('#end_date').innerHTML;
    }
};

