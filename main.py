from flask import Flask, send_file
from dotenv import load_dotenv
import os
from pyngrok import ngrok
import pyshorteners

url = ngrok.connect(5000)
print("Ngrok URL:", url)

url_convertida = url.public_url

encurtador = pyshorteners.Shortener()
url_encurtada = encurtador.tinyurl.short(str(url_convertida))
print("URL encurtado:", url_encurtada)

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/ep1')
def ep1():
    return send_file(os.getenv('EP1'))

@app.route('/ep2')
def ep2():
    return send_file(os.getenv('EP2'))

@app.route('/ep3')
def ep3():
    return send_file(os.getenv('EP3'))
@app.route('/ep4')
def ep4():
    return send_file(os.getenv('EP4'))
@app.route('/ep5')
def ep5():
    return send_file(os.getenv('EP5'))
@app.route('/ep6')
def ep6():
    return send_file(os.getenv('EP6'))
@app.route('/ep7')
def ep7():
    return send_file(os.getenv('EP7'))
@app.route('/ep8')
def ep8():
    return send_file(os.getenv('EP8'))
@app.route('/ep9')
def ep9():
    return send_file(os.getenv('EP9'))
@app.route('/ep10')
def ep10():
    return send_file(os.getenv('EP10'))
@app.route('/ep11')
def ep11():
    return send_file(os.getenv('EP11'))
@app.route('/ep12')
def ep12():
    return send_file(os.getenv('EP12'))




app.run()
