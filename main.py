from flask import Flask, request

app = Flask(__name__)


@app.route('/contact', methods=['GET', 'POST'])
def handle_request():
    data = request.form
    print(data)
    return 'Handling contacts'


if __name__ == "__main__":
    app.run()
