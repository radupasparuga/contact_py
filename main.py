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
        conn = psycopg2.connect(dbname="contact", user="postgres", password=cfg.pwd, port="7571")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute('INSERT', (request.form['name'], request.form['email'], request.form['message']))
    conn.commit()
    print(data)
    cur.close()
    conn.close()
    return 'Handling contacts'


if __name__ == "__main__":
    app.run()
