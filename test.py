from flask import Flask, request
import psycopg2

app = Flask(__name__)

try:
    conn = psycopg2.connect(dbname="contact", user="postgres", host="localhost", password="password")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("SELECT * FROM persons.persons;")



if __name__ == "__main__":
    app.run()
