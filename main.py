from flask import Flask
# Required for ngrok to run flask on a public URL
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# Run flask on a public URL
run_with_ngrok(app)
# Run the app, matched to the URL
if __name__ == '__main__':
    #launches app on localhost:5000
    app.run()