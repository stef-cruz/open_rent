let durationOfTenancy = document.querySelectorAll('.js-duration-of-tenancy');
let tenancies = document.querySelectorAll('.js-card-tenancy-profile');
let startDates = document.querySelectorAll('.js-start-date');
let endDates = document.querySelectorAll('.js-end-date');

//Calculate years, months and days, adapted from source https://stackoverflow.com/questions/12251325/javascript-date-to-calculate-age-work-by-the-day-months-years
for (let i = 0; i < tenancies.length; i++) {

    let startDate = new Date(startDates[i].innerHTML);
    console.log(startDate)
    let endDate = new Date(endDates[i].innerHTML);
    console.log(endDate)

    let years = endDate.getFullYear() - startDate.getFullYear();
    console.log(years)
    let months = endDate.getMonth() - startDate.getMonth();
    console.log(months)
    let days = endDate.getDate() - startDate.getDate();
    console.log(days)

    // Work out the difference in months.
    months += years * 12;
    if (days < 0) {
        months -= 1;
    }

    // Now add those months to the end date.
    endDate.setMonth(startDate.getMonth() + months);

    // Calculate the difference in milliseconds.
    let diff = endDate - startDate;
    // Divide that by 86400 to get the number of days.
    days = Math.round(diff / 86400 / 1000);
    // Now convert months back to years and months.
    years = parseInt(months / 12);
    months -= (years * 12);
    // Format date as "xx years, yy months, zz days"
    let output = "";
    if (years) {
        output = years + (years > 1 ? " years" : " year");
    }
    if (months) {
        if  (output.length) {
            output = output + ", ";
        }
        output = output + months + (months > 1 ? " months" : " month")
    }
    if (days) {
        if  (output.length) {
            output = output + ", ";
        }
        output = output + days + (days > 1 ? " days" : " day")
    }
    durationOfTenancy[i].innerHTML = output;
}

