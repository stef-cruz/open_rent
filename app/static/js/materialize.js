// MATERIALIZE INITS

document.addEventListener('DOMContentLoaded', function() {
    //Home page, side nav
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems,{edge: "right"});
    //Profile page, select dropdown
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    //Profile page, date picker
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems,
        {yearRange: 15,
            format: 'dd mmmm yyyy'
        });
});
