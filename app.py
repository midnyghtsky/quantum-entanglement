from flask import Flask, Response
app = Flask(__name__)
import requests  # keep the module unshadowed
import quant as q

@app.route('/')
def hello_world():
    r = q.q()  # get the drawing object
    # Return as plain text so whitespace/newlines are preserved exactly
    return Response(str(r), mimetype='text/plain')


if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run()