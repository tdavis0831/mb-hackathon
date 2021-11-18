"""Server for final project"""
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "fvdrgdtuntryktuit8578r6bw345vwv"
app.jinja_env.undefined = StrictUndefined




@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")



@app.route("/create-account")
def create_account():

    return render_template("create-account.html")






@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    name= request.form.get("name")

    user = crud.get_user_by_email(email)
    
    if user:
        flash("Email already associated with account, try logging in")
    else:
        crud.create_user(email, password, name)
        flash("Account created! Please log in.")

    return redirect("/")






@app.route("/login", methods=["POST", "GET"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")
    name=request.form.get("name")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's id in session
        session["user_id"] = user.user_id
        session["name"] = user.name
        
        

    return render_template("user-profile.html", user=user)






if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)