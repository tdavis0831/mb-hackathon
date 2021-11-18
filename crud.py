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



def create_anime(anime_name, episode_title, episode_length, fk_user_id):

    episode_entry=Anime(anime_name=anime_name, episode_title=episode_title, episode_length=episode_length, fk_user_id=fk_user_id)

    db.session.add(episode_entry)
    db.session.commit()

    return episode_entry


def create_future_anime(anime_name, fk_user_email):

    future_episode_entry=FutureAnime(anime_name=anime_name, fk_user_email=fk_user_email)

    db.session.add(future_episode_entry)
    db.session.commit()

    return future_episode_entry

