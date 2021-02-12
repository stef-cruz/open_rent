//Code adapted from source https://codepen.io/luv2code/pen/oNvrWyZ

// Create default dates
var date = new Date();
// set default date for #start_date (1 week from today)
var nextWeekStartDate = new Date(date.setDate(date.getDate() + 7));
// Default date for #end_date
var nextWeekEndDate = new Date(date.setDate(nextWeekStartDate.getDate() + 7));

// SET OPTIONS FOR #start_date
var optionsStartDate = {
    defaultDate: new Date(nextWeekStartDate),
    autoClose: true,
    showClearBtn: true,
    format: 'dd mmmm yyyy',
    onSelect: function(el) {
        const ell = new Date(el);
        const setMM = ell.getDate();
        const setMonth = new Date(ell.setMonth(date.getMonth()+1))
        const setM = new Date(ell.setDate(setMM));
        setMinEndDate(setM);
    }
};


// SET OPTIONS FOR #end_date
var optionsEndDate = {
    defaultDate: new Date(nextWeekEndDate),
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
var setMinEndDate = function(element) {
    // Get the current date set on #end_date datepicker
    var instance = M.Datepicker.getInstance(document.querySelector('#end_date'));
    instance.options.minDate = element;

    // Check if the #start_date date is greater than the #end_date date and modify by 1 day if true.
    if (new Date(instance) < element) {
        instance.setDate(element);
        document.querySelector('#end_date').val(instance.toString());
    }
};

