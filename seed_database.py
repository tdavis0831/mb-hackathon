"""Script to seed database."""

import os


import crud
import model
import server


os.system("dropdb animes")
os.system("createdb animes")

model.connect_to_db(server.app)
model.db.create_all()


