from flask import Flask, request


app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "webhook is running...!"
    
    if request.method == 'POST':
        body = request.get_json()
        print(body)

        return {'message': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)
