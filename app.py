from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'


api_url = 'https://api.telegram.org'
token = '1067262815:AAEhempCvWub8rd7Wk_3dffbS8toDRK8v4w'
chat_id = '1039258753'
@app.route('/send/<text>')
def sedn(text):
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return 'ok!'


app.run(debug=True)