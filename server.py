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
        session["email"] = user.email
        
        

    return render_template("user-profile.html", user=user)

@app.route("/log")
def watched_anime_log():


    return render_template("log.html")

@app.route("/future-log")
def future_anime_log():
    return render_template("future-log.html")


@app.route("/create-log", methods=["POST"])
def create_log():
    anime_name = request.form.get("anime_name")
    episode_title = request.form.get("episode_title")
    episode_length = request.form.get("episode_length")
    fk_user_id= session["user_id"] 

    
    anime_added=crud.create_anime(anime_name, episode_title, episode_length, fk_user_id)

    return render_template("anime-added.html", anime_name=anime_name)


@app.route("/create-watch-log", methods=["POST"])
def create_future_log():
    anime_name = request.form.get("anime_name")
    fk_user_id= session["email"] 
    

    
    future_anime_added=crud.create_future_anime(anime_name, fk_user_id)
    
    return render_template("anime-added.html", anime_name=anime_name)



@app.route("/all-anime")

def all_anime():
    animes=crud.get_animes()

    return render_template("all-animes.html", animes=animes)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)