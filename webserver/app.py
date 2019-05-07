from flask import Flask, render_template, jsonify
import csv
import sys, os
sys.path.append('21_ftp')
import ftpclient as ftp

reading = "Not downloaded yet"

if not os.path.exists("client-output"):
    os.makedirs("client-output")

log_file_path = "client-output/log.csv"

app = Flask(__name__)


@app.route('/update')
def update(name=None):
    global reading 
    fetchTemps()
    reading = getReading()
    return jsonify({"status": "ok", "newReading": reading})

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    global reading 
    return render_template('index.html', name=name, reading=reading)


def fetchTemps():
    ftp_client = ftp.FTPClient("192.168.21.5", 21)
    ftp_client.connect()
    ftp_client.login()
    print(ftp_client.retrlines("LIST"))
    # the false means do not print contents to stdout
    print(ftp_client.retrlines("RETR log.csv"))



def getReading():
    global reading
    if reading == "Not downloaded yet":
        reading = 0
    with open(log_file_path) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if len(row) >= 4 and row[4] != 'GyrX':
                val = int(row[4])
                if val > reading:
                    reading = val
    return reading

if os.path.isfile(log_file_path):
    getReading()
