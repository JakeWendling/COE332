import xmltodict
import requests
from flask import Flask

app = Flask(__name__) 

@app.route('/', methods=['GET'])
def getData():
    response = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    return data

@app.route('/epochs', methods=['GET'])
def getEpochs():
    response = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    stateList = data['ndm']['oem']['body']['segment']['data']['stateVector']
    epochs = []
    for state in stateList:
        epochs.append(state['EPOCH'])
    return epochs

@app.route('/epochs/<epoch>', methods=['GET'])
def getStateVector(epoch):
    response = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    stateList = data['ndm']['oem']['body']['segment']['data']['stateVector']
    for state in stateList:
        if state['EPOCH'] == epoch:
            return state
    return "Error: Epoch not found", 400

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def getSpeed(epoch):
    response = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    stateList = data['ndm']['oem']['body']['segment']['data']['stateVector']
    for state in stateList:
        if state['EPOCH'] == epoch:
            x_dot = float(state['X_DOT']['#text'])
            y_dot = float(state['Y_DOT']['#text'])
            z_dot = float(state['Z_DOT']['#text'])
            speed = (x_dot**2 + y_dot**2 + z_dot**2)**.5
            return f"{str(speed)} {state['Z_DOT']['@units']}\n"
    return "Error: Epoch not found\n", 400
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
