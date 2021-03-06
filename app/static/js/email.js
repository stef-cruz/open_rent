//Initialise emailJS
(function () {
    emailjs.init("user_Oay0ciCVLZ3t84nUMqX94");
})();

let forms = document.getElementById('contact-form');

forms.addEventListener('submit', function(evt){
    evt.preventDefault();
    emailjs.sendForm('gmail', 'milestone3', '#contact-form')
        .then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
            document.getElementById("js-positive-feedback").style.display = "block";
        }, function (error) {
            console.log('FAILED...', error);
            document.getElementById("js-negative-feedback").style.display = "block";
        });
});