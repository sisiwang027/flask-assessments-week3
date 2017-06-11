from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE


@app.route("/")
def show_index():
    #show home page.
    return render_template("index.html")


@app.route("/application-form")
def take_application():
    #take user's application. job_list is a list storing all job titles.
    job_list = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", job_list=job_list)


@app.route("/application-success")
def show_application():
    #show the application message.
    lastname = request.args.get("lastname")
    firstname = request.args.get("firstname")
    salary = format(float(request.args.get("salary")), ',.2f')
    jobtitle = request.args.get("jobtitle")
    
    return render_template("application-response.html", lastname=lastname, 
                            firstname=firstname, salary=salary, jobtitle=jobtitle)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
