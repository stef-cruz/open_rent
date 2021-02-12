// MATERIALIZE INITS

document.addEventListener('DOMContentLoaded', function() {
    //Home page, side nav
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems,{edge: "right"});
    //Profile page, select dropdown
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    //Profile page, Collapsible
    var elems = document.querySelectorAll('.collapsible.expandable');
    var instances = M.Collapsible.init(elems, {
        accordion: false
    });
    //Profile page, delete tenancy button
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

