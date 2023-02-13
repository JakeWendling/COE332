import requests
import json
import math

def getJson(url_string: str) -> dict:
    """
    Retrieve a JSON response from a given URL string and return the result as a dictionary.

    Args:
        url_string (str): The URL to send a GET request to.

    Returns:
        dict: The JSON response as a dictionary.
    """
    response = requests.get(url=url_string)
    return response.json()

def calcTurbidity(a0: float, I90: float) -> float:
    """
    Calculate the turbidity in NTU units based on the calibration constant and detector current.

    Args:
        a0 (float): The calibration constant.
        I90 (float): The 90-degree detector current.

    Returns:
        float: The calculated turbidity in NTU units (0-40).
    """
    T = abs(a0 * I90)
    return T

def calcMinTime(T0: float, d: float, Ts: float) -> float:
    """
    Calculate the minimum time required to return below a safe threshold.

    Args:
        T0 (float): The current turbidity.
        d (float): The decay factor per hour, expressed as a decimal.
        Ts (float): The turbidity threshold for safe water.

    Returns:
        float: The minimum time required in hours.
    """
    b = math.log(Ts / T0) / math.log(1 - d)
    return b

def calcTurbidityAverage(turb_data: dict, turb_key: str, cc_key: str, dc_key: str) -> float:
    """
    Calculate the average of the last five samples of turbidity data.

    Args:
        turb_data (dict): The dictionary containing the turbidity data.
        turb_key (str): The key of the turbidity data in the dictionary.
        cc_key (str): The key of the calibration constant in the dictionary.
        dc_key (str): The key of the detector current in the dictionary.

    Returns:
        float: The average of the last five samples of turbidity.
    """
    turbidity_sum = 0.0
    data_count = min(5, len(turb_data[turb_key]))
    for sample in turb_data[turb_key][-5:]:
        calibration_constant = sample[cc_key]
        detector_current = sample[dc_key]
        turbidity_sum += calcTurbidity(calibration_constant, detector_current)
    turbidity_average = turbidity_sum / data_count
    return turbidity_average
    
def main():
    url = 'https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json'
    turb_data = getJson(url)
    decay_factor = 0.02
    turbidity_threshold = 1.0
    turb_data['turbidity_data'] = sorted(turb_data['turbidity_data'],key=lambda d: d['datetime'])

    turbidity_average = calcTurbidityAverage(turb_data, 'turbidity_data', 'calibration_constant', 'detector_current')
    print(f'Average turbidity based on most recent five measurements = {turbidity_average} NTU')
    if turbidity_average > turbidity_threshold:
        time_until_safe = calcMinTime(turbidity_average, decay_factor, turbidity_threshold)
        print('Warning: Turbidity is above threshold for safe use')
    else:
        time_until_safe = 0.0
        print('Info: Turbidity is below threshold for safe use')
    print(f'Minimum time required to return below a safe threshold = {time_until_safe} hours')
            
if __name__ == '__main__':
    main()
