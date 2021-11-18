from model import db, User, Anime, FutureAnime, connect_to_db

def get_animes():
    return db.session.query(Anime).all()



def create_user(email, password, name):
    #creates a user

    user=User(email=email, password=password, name=name)
    
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()   



def create_anime(anime_name, episode_title, episode_length):

    episode_entry=Anime(anime_name=anime_name, episode_title=episode_title, episode_length=episode_length)

    db.session.add(episode_entry)
    db.session.commit()

    return episode_entry



