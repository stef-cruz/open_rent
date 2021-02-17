let durationOfTenancy = document.querySelectorAll('.js-duration-of-tenancy');
let tenancies = document.querySelectorAll('.js-card-tenancy-profile');
let startDates = document.querySelectorAll('.js-start-date');
let endDates = document.querySelectorAll('.js-end-date');

//Month difference function source https://stackoverflow.com/questions/2536379/difference-in-months-between-two-dates-in-javascript
function monthDiff(dateFrom, dateTo) {
    return dateTo.getMonth() - dateFrom.getMonth() +
        (12 * (dateTo.getFullYear() - dateFrom.getFullYear()))
}

for (let i = 0; i < tenancies.length; i++) {
    let startDate = new Date(startDates[i].innerHTML);
    let endDate = new Date(endDates[i].innerHTML);

        if (monthDiff(startDate, endDate) < 0 || monthDiff(startDate, endDate) === 0) {
            durationOfTenancy[i].innerHTML = 'Less than 1 month'
        } else if (monthDiff(startDate, endDate) === 1) {
            durationOfTenancy[i].innerHTML = '1 month'
        } else {
            durationOfTenancy[i].innerHTML = `${monthDiff(startDate, endDate)} months`
        }
}

