import xmltodict
import requests
from typing import List#,String
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getData() -> dict:
    """
    Gets the nasa ISS location data and returns the data in dictionary format

    Returns:
        data: The ISS coordinate data in dictionary format.
    """
    response = requests.get('https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
    data = xmltodict.parse(response.text)
    return data

@app.route('/epochs', methods=['GET'])
def getEpochs() -> List[str]:
    """
    Gets the nasa ISS location data and returns the list of epochs in dictionary format
    
    Returns:
        epochs: a list of epochs(strings) for which ISS coordinate data is available.
    """
    data = getData()
    stateList = data['ndm']['oem']['body']['segment']['data']['stateVector']
    epochs = []
    for state in stateList:
        epochs.append(state['EPOCH'])
    return epochs

@app.route('/epochs/<epoch>', methods=['GET'])
def getStateVector(epoch: str) -> dict:
    """
    Gets the nasa ISS location data, 
    then returns the state vector for a given epoch, if available. 
    Otherwise returns an error message and error code.
    
    Args:
        epoch: A string representing an epoch.
        
    Returns:
        state:  The state vector for the given epoch, if available. 
    
    Raises:
        If no state vector is available for the given epoch, 
        returns an error message and a 400 status code.
    """
    data = getData()
    stateList = data['ndm']['oem']['body']['segment']['data']['stateVector']
    for state in stateList:
        if state['EPOCH'] == epoch:
            return state
    return "Error: Epoch not found\n", 400

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def getSpeed(epoch: str) -> float: 
    """
    Gets the nasa ISS location data, 
    then returns the state vector for a given epoch, if available. 
    Otherwise returns an error message and error code.
    
    Args:
        epoch: A string representing an epoch.
        
    Returns:
        speed: A float representing the speed of the ISS at the given epoch, if available. 

    Raises:
        If no speed is available for the given epoch, 
        returns an error message and a 400 status code.
    """
    data = getData()
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
