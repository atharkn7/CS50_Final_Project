# **MAKEUP STUDIO Website**
#### Video Demo:  https://youtu.be/quAgaE3p_h8
#### Description:
The **Makeup Studio Website** serves as the digital face of the studio, providing information about services, enabling client bookings, and handling client queries. It is designed to be user-friendly, visually appealing, and functional.

## Tech Stack
- **Frontend**: HTML, CSS (Bootstrap for fonts), JavaScript
- **Backend**: Python (Flask), SQLite3

# File
### `app.py`
This is the main Flask application file that handles routing, database interactions, and user requests.

#### **Libraries Imported**
- **cs50.SQL**: Used to interact with the SQLite database.
- **Flask**: The core framework for building the web application.
- **render_template**: Renders HTML templates for each route.
- **request**: Handles HTTP requests (GET/POST) and retrieves form data.
- **redirect**: Redirects users to different routes based on conditions.
- **re**: Used for regex validation of user inputs.

#### **Database**
- The database is initialized using the `cs50.SQL` class and is stored in a variable `db`

#### **Routes**
- **Home (`/`)**:
    - The landing page, rendered using `layout.html` (defines the general layout) and `index.html` (contains the main content).
    - **Design Decision**: All routes have been given the property of `active_page` which allows us to highlight currently active page on the navbar.
- **Services (`/services`)**:
  - **GET**: Displays the services page (`services.html`).
    - **Design Decision**: *layout.html* has been designed to show a navbar that allows the user can click on `Services` or if they hover over it they will get a dropdown of all services provided. In case the user clicks on one of the services in the dropdown the content on `services.html` changes based on user selection.
        - The change is handled by using the `service` property that stores what value was selected by user which is then sent to the `services.html` template
  - **POST**: Handles form submissions from the services page (e.g., service booking requests).
    - In case of form submission all values are first stored in variables.
    - Allowed inputs for *phone_number* & *VALID_SERVICES* are also stored in variables
    - **Design Decision:**
        - error handing is done by initially creating an empty variable called `error`. Then depending on the type of validation error create by user input value of *error* is update to a dictionary which has the error message and the error code.
        - This has been done so that in case of an error, `error` will not be blank and will have a value and that can be dynamically added to an `apology.html` webpage.
    - In case of no errors, user data as added to the bookings table in the database. The user is then redirected back to the homepage.
- **About** (`/about`):
    - **GET**: Displays `about.html` template and has `active_page` value set to "about" to dynamically update the navbar.
    - **POST**: This webpage contains the a form allowing user to submit a general query using just their name & phone number.
        - Form data is accessed using `request`
        - Similar to *services* route validation is done and the value of `error` is updated in case there is an error found.
        - In case of no errors, user data is added to queries table in the database. The user is then redirected to homepage.

### `makeover.db`
This is the main database file currently containing 2 tables -
* **bookings**: Contains the following fields
    - `booking_id`: Primary Key Autoincrementing
    - `name`
    - `phone_number`
    - `email`
    - `service_booked`
    - `appointment_date`
    - `booking_time`: captured automatically on data insertion using `CURRENT_TIMESTAMP`
* **queries**: Contains the following fields
    - `query_id`: Primary Key Autoincrementing
    - `name`
    - `phone_number`
    - `query_time`: To save when the query was sent
    - `message`

### `requirements.txt`
Lists all dependencies for the project
- cs50
- flask
- re

## Static Files
### `script.js`
This file currently has 3 main functions inside it to make the website more dynamic. All functions are executed once the document has loaded and hence have been added inside it -
1. **Navbar**: This function has an event listener on user scroll.
    - in case the user is at the top of the page, i.e., scroll value is currently 0 then it changes the height of the navbar 150px.
    - Once the user scrolls down the navbar is reduce to 80px.
    - **Design Decision:** The purpose of this function is to show a dynamically changing navbar based on user interaction.
2. **Service Image:** This function changes the image on the `services.html`  template based on which option user has selected at the time of booking their appointment.
3. **Calendar Validation:** Restricts users to only select a date from today to today + 14 days while booking an appointment.

### `styles.css`
Entire website has been styled using this file. It has been used to define various features, such as, **layout**, **animation**, **transitions**, **dropdowns** etc., of the website which have been explained in more detail in the templates section of this README.


## Templates

### `layout.html`

This template defines the general layout of the entire website. Entire template has been styled using `styles.css`. It divides the webpage into 3 main sections:
- `<nav>` - The nav section is further divided into 2 sections using the **flexbox** propery of CSS.
    - First section on the left contains the business Logo
    - Section on the right contains links to different routes.
        - These links are accessible from each route in the website as navbar content is uniform throughout the website.
        - **Services Dropdown:** has been created to show itself just below the relevant nav item. This is done by initially setting its value to `display: none`. However, in case the hovers over the "Services" in the navbar the value updates to `display: flex`.
- `<footer>`
    - Flex box have been used in this section to create the layout at the bottom of the screen for the footer.
    - Footer is further divided into 4 container each of which are flex boxes as well that contain links to various sections of the webpage allowing easier navigation.
    - Also, this section contains contact information about the business's contact information for the users.
- **Design Decisions:** primarily use of `Jinja` has been done to create a more dynamic experience for the user.
    1. `active_page`: property has been used to get the currently active page and highlight it in the navbar to visually show the user where they are.
    2. `<main>`: This main part of the website has been dynamically updated from different templates using jinja as well.

### `index.html`
This template contains the main content for the landing page. Entire template has been styled using `styles.css`. It is divided into 4 sections.
1. **Hero:** The hero section contains the brand logo, along with the brand tagline. It has a button allowing user to directly jump to bookings. The button links to the `/services` and jumps the user straight to the booking form.
2. **Infinite Scroll:** This section features past client images for the business as a showcase of their work. This has been converted to an infinite scrolling carousel that freezes in case the user hovers over this section.
    - **Keyframes** have been used to move the images along their **X Axis**.
    - Further, upon hover the individual images change scale, this design has been implemented in `styles.css`.
3. **Benefits section:** lists benefits of using the business services. These have been implemented in further 4 sections using **flexbox** as well.
4. **Lower Section:** contains further content for the business. Again layout & design has been implemented using **flexbox**.
    - `BOOK NOW` button takes the user to `/services` and jumps the user straight to the booking form.

### `services.html`

This template is accessed via the `/services` route from `app.py`. Entire template has been styled using `styles.css` It has been divided into 2 main sections, The layout of both sections is done using **flexbox**. -

1. **Upper Section:**  It is further divided into 2 sections -
    - **Left:** This contains an image. This image updates based on which option was selected by the user from the dropdown or in case the user simply clicked on **services**.
        - This image is dynamically updated using `Jinja`, the property `services` is used to check the value selected by user to show different images.
    - **Right:** Jinja conditionals are used in this section to show different content based on value of `services`.
2. **Lower Section:** This contains the booking form allowing user to create a booking. The layout has been done using `display: grid` property in CSS to divide the form into a 3x3 grid.
    - `input` fields are placed in the first 2 rows. Various types of inputs are collected, `first_name`, `last_name`, `phone_number`, `email`, `service`, `appointment_date`.
    - For the `service` dropdown **Jinja** has been used to dynamically select the option that user has selected from the navbar dropdown.
    - `BOOK NOW` button sends a `POST` request to the server submitted user entered data to be validated and entered in the `bookings` table in the database.

### `about.html`
This template is accessed via the `/about` route from `app.py`. Entire template has been styled using `styles.css` It has been divided into 3 main sections, the layout is done using `display: grid`
1. `about-grid1`: Contains a shorter contact form where user can enter just their name, number along with a custom message to send a general query rather than doing an entire booking.
    - The form sends a `POST` request to the server, where the user input is validated and entered into `queries` table in the database.
2. `about-grid2`: This grid contains a **flexbox** to show user all contact information if they directly want to contact the business.
3. `about-grid3`: Spans 2 column lengths to show an embedded Google Map of the business to allow the convenience of directly using Google Maps to create a route to the business for the clients.
    - The map has been embedded using an `iframe` taken from Google Maps.

### `apology.html`
This template works as a error page in case the user input fails **validation checks** at the backend. The user is shown why there was an error along with an error code and an image to add some graphical content to the page.
- A button has been added to allow the user to be go back to the homepage and try again.

# Future Improvements
- Add user authentication for business employees to view bookings.
    - Integrate booking in a way which shows available time for appointments as well.
- Integrate a payment gateway for online payments.