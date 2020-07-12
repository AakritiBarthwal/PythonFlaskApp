from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/appicationDeveloperName')
def hello_world2():
    return 'Created by Aakriti'

app.run(port=50000)