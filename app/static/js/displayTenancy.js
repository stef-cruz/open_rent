// Display tenancy details when marker is clicked

//Function to wait for the insertion of the element #js-infowindow__lat into the DOM. Source https://stackoverflow.com/questions/5525071/how-to-wait-until-an-element-exists

function waitForElementToDisplay(selector, callback, checkFrequencyInMs, timeoutInMs) {
    var startTimeInMs = Date.now();
    (function loopSearch() {
        if (document.querySelector(selector) != null) {
            displayTenancy();
            return;
        } else {
            setTimeout(function () {
                if (timeoutInMs && Date.now() - startTimeInMs > timeoutInMs)
                    return;
                loopSearch();
            }, checkFrequencyInMs);
        }
    })();
}

function displayTenancy() {

    //Get number of tenancies on rent-register.html
    let cardTenancies = document.getElementsByClassName("js-card-tenancy");

    //Clear previous results
    for (let j = 0; j < cardTenancies.length; j++) {
        if (cardTenancies[j].style.display = "block") {
            cardTenancies[j].style.display = "none";
        }
    }

    //Get Lat & Long from rent-register.html
    let rentsMapLat = document.getElementsByClassName("js-lat");
    let rentsMapLong = document.getElementsByClassName("js-long");


    //Get Lat & Long from infoWindow
    let infoWindowLat = document.getElementById("js-infowindow__lat").innerHTML;
    let infoWindowLong = document.getElementById("js-infowindow__long").innerHTML;

    for (let i = 0; i < cardTenancies.length; i++) {
        //if lat long from infoWindow == lat long from tenancies on rent-register.html, display: block
        if (rentsMapLat[i].innerHTML == infoWindowLat && rentsMapLong[i].innerHTML == infoWindowLong) {
            cardTenancies[i].style.display = "block";
        }
    }
}

