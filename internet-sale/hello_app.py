from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!охуэннасска'

if __name__ == '__main__':
    app.run(debug=True)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#

# print('Huilo!')
#https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP
