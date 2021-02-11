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
    var instances = M.Datepicker.init(elems, {
            yearRange: 15,
            format: 'dd mmmm yyyy',
            showClearBtn: true,
        });
    //Profile page, Collapsible
    var elems = document.querySelectorAll('.collapsible.expandable');
    var instances = M.Collapsible.init(elems, {
        accordion: false
    });
    //Profile page, delete tenancy button
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);


    //Validate materialize select input, source https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
        let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
        let dataErrorText = document.querySelector('#js-helper-text-select');
        let selectValidate = document.querySelector("select.validate");
        let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
        if (selectValidate.hasAttribute("required")) {
            selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
        }
        selectWrapperInput.addEventListener("focusin", (e) => {
            e.target.parentNode.addEventListener("change", () => {
                ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
                for (let i = 0; i < ulSelectOptions.length; i++) {
                    if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                        e.target.style.cssText = classValid;
                            if (e.target.style.cssText = classValid) {
                                dataErrorText.style.display = "none";
                            }
                    }
                }
            });
        });
        selectWrapperInput.addEventListener("click", (e) => {
            ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
            for (let i = 0; i < ulSelectOptions.length; i++) {
                if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                    e.target.style.cssText = classValid;
                        if (e.target.style.cssText = classValid) {
                            dataErrorText.style.display = "none";
                        }
                } else {
                    e.target.addEventListener("focusout", () => {
                        if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                            if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                                e.target.style.cssText = classInvalid;
                                if (e.target.style.cssText = classInvalid) {
                                    dataErrorText.style.display = "block";
                                }
                            }
                        }
                    });
                }
            }
        });
    }

});