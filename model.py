from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """a user"""

    __tablename__= "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password= db.Column(db.String(50))
    name=db.Column(db.String(50))
    
    def __repr__(self):
   
    	return f"<user_id = {self.user_id} email={self.email}>"


class Anime (db.Model):
	"""an anime"""

	__tablename__="animes"

	anime_id =db.Column(db.Integer, autoincrement=True, primary_key=True)
	anime_name = db.Column(db.String, unique=True)
	episode_title = db.Column(db.String)
	episode_length = db.Column(db.Integer)
	fk_user_id= db.Column((db.Integer), db.ForeignKey("users.user_id"))

	animes = db.relationship("User", backref="animes")


class FutureAnime (db.Model):

    __tablename__: "future-animes"

    
    anime_id =db.Column(db.Integer, autoincrement=True, primary_key=True)
    anime_name = db.Column(db.String, unique=True)
    fk_user_id= db.Column((db.Integer), db.ForeignKey("users.user_id"))

    future_animes = db.relationship("User", backref="future-animes")



	




def connect_to_db(flask_app, db_uri="postgresql:///animes", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] =  db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected")




if __name__ == "__main__":
	from server import app

    # print(db.metadata.tables)



	connect_to_db(app)