import time

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Steve1!'

@app.route('/foo')
def foo():
	x = 1+666
	return "THE VALUE IS: %s" % x

@app.route('/time')
def timer():
	return "The time is: %s" time.time()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
