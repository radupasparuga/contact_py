from flask import Flask, request
import psycopg2
import yaml

app = Flask(__name__)

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


@app.route('/contact', methods=['GET', 'POST'])
def handle_request():
    data = request.form
    try:
        conn = psycopg2.connect(dbname="contact", user="postgres", password=cfg['dbpwd'], host="localhost")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute("INSERT INTO persons.persons (name, email, message) VALUES  (%s, %s, %s)", (request.form['name'], request.form['email'], request.form['message']))
    conn.commit()
    print(data)
    cur.close()
    conn.close()
    return 'Handling contacts'


if __name__ == "__main__":
    app.run()
