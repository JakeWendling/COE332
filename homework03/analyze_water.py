#!/usr/bin/env python3

import requests
import json
import math

def getJson(url_string):
    response = requests.get(url=url_string)
    return response.json()

def calcTurbidity(a0, I90):
    '''
    T = a0 * I90
    T = Turbidity in NTU Units (0 - 40)
    a0 = Calibration constant
    I90 = Ninety degree detector current
    '''
    T = abs(a0 * I90)
    return T
    
def calcMinTime(T0, d, Ts):
    '''
    Ts > T0(1-d)**b
    Ts = Turbidity threshold for safe water
    T0 = Current turbidity
    d = decay factor per hour, expressed as a decimal
    b = hours elapsed
    '''
    b = math.log(Ts / T0) / math.log(1 - d)
    
    return b

def calcTurbidityAverage(turb_data, turb_key, cc_key, dc_key):
    '''
    Takes the last five samples and returns the average of the turbdidty
    '''
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
