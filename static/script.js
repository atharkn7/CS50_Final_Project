document.addEventListener('DOMContentLoaded', function () {
    // Reducing size of navbar as user scrolls
    let navbar = document.querySelector('nav');

    window.addEventListener('scroll', function () {
        let scroll = document.documentElement.scrollTop;

        if (scroll > 0) {
            navbar.style.height = "80px";
        }
        else {
            navbar.style.height = "150px";
        }
    })

    // Changing image based on option selected in dropdown
    let select = document.querySelector("#service");
    let service_img = document.querySelector("#service-img");

    select.addEventListener('change', function () {
        let selectedValue = select.value; // Get selected dropdown value
        service_img.src = `/static/media/service_imgs/${selectedValue}.jpg`;
        service_img.alt = selectedValue.replace(/_/g, " ");
    })


    // Having only valid values in calendar
    let today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD formatting (From ChatGPT)

    // Setting max date to 14 days
    let max_date = new Date();
    max_date.setDate(max_date.getDate() + 14);
    max_date = max_date.toISOString().split('T')[0]; // YYYY-MM-DD formatting (From ChatGPT)

    let date_input = document.querySelector("#appointment_date")

    // Setting value
    date_input.setAttribute("min", today);
    date_input.setAttribute("max", max_date);
})
