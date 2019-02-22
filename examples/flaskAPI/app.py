from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action')
# ip:port?dir=go / ip:port?dir=back
def action():

    dir = request.args.get('dir')

    if dir == 'go':
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.cleanup()
        return 'GO GO GO!'
    elif dir == 'back':
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        time.sleep(5)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        GPIO.cleanup
        return 'Ok, go back.'
    else:
        return 'Not found'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
