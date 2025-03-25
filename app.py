from cs50 import SQL
from flask import Flask, render_template, request, redirect
import re

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///makeover.db")


@app.route("/")
def index():
    return render_template("index.html", active_page="home")


@app.route("/services", methods=["GET", "POST"])
def services():
    # GET
    if request.method == "GET":
        # Getting the service selected by user
        service = request.args.get("service")

        if service == None:
            # If just clicked on services at the top
            return render_template("services.html", active_page="services", service='', service_value='')

        if service != "":
            # Modifying page based on what value selected by user
            service_value = service.replace("_", " ").upper()
            return render_template("services.html", service=service, service_value=service_value, active_page="services")

    # POST
    else:
        # Getting & Validating Form Data
        fname = request.form.get("first_name").strip()
        lname = request.form.get("last_name").strip()
        phone_number = request.form.get("phone_number")
        email = request.form.get("email").strip()
        service = request.form.get("service").strip()
        appointment_date = request.form.get("appointment_date")

        # Allowed inputes
        phone_regex = re.compile(r"^[6-9]\d{9}$")  # Regex pattern for Indian numbers (ChatGPT)
        VALID_SERVICES = {
            "bridal_airbrush_makeup",
            "bridal_makeup",
            "engagement_makeup",
            "party_makeup",
            "hair_highlights",
            "hair_keratin_treatment",
            "ozone_hair_treatment",
            "hair_styling",
        }

        # Initializing error value
        error = ""

        # Required field validation
        if not fname or not lname or not phone_number or not email or not service or not appointment_date:
            error = {"error": "Required information not entered",
                     "code": 400}

        # Checking alphabetical name
        if not fname.isalpha() or not lname.isalpha():
            error = {"error": "Invalid name",
                     "code": 400}

        # Combining name
        name = fname + " " + lname

        # Phone number validation (ChatGPT)
        if not phone_regex.match(phone_number):
            error = {"error": "Invalid phone number format",
                     "code": 400}

        # Service dropdown validation
        if service not in VALID_SERVICES:
            error = {"error": "Invalid service selection",
                     "code": 400}

        if not error:
            db.execute("INSERT INTO bookings (name, phone_number, email, service_booked, appointment_date) VALUES (?, ?, ?, ?, ?)",
                       name, phone_number, email, service, appointment_date)
            return redirect("/")
        else:
            # Showing user an apology incase of errors
            return render_template("apology.html", error=error)


@app.route("/about", methods=["GET", "POST"])
def about():

    # POST
    if request.method == "POST":
        # Getting & Validating Form Data
        name = request.form.get("name").strip()
        phone_number = request.form.get("phone_number")
        message = request.form.get("message").strip()

        # Allowed inputes
        phone_regex = re.compile(r"^[6-9]\d{9}$")  # Regex pattern

        # Initializing error value
        error = ""

        if not name or not phone_number:
            error = {"error": "Required information not entered",
                     "code": 400}

        if not name.isalpha():
            error = {"error": "Invalid name",
                     "code": 400}

        if not phone_regex.match(phone_number):
            error = {"error": "Invalid phone number format",
                     "code": 400}

        if not error:
            db.execute("INSERT INTO queries (name, phone_number, message) VALUES (?, ?, ?)",
                       name, phone_number, message)
            return redirect("/")
        else:
            # Showing user an apology incase of errors
            return render_template("apology.html", error=error)

    # GET
    else:
        return render_template("about.html", active_page="about")
