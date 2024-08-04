import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgredb_fhxv_user:51nNP8m3ASnZH53Oko1DRop8ZM61Ggc4@dpg-cql5meg8fa8c73cv7h7g-a.oregon-postgres.render.com/postgredb_fhxv'