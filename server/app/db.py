from flask_sqlalchemy import SQLAlchemy
import psycopg2

CREATE_DB = "CREATE DATABASE IF NOT EXISTS bondgames"
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS games (id SERIAL PRIMARY KEY, name TEXT)"
INSERT_GAME = "INSERT INTO games (name) VALUES (%s) RETURNING id"
db = SQLAlchemy()


