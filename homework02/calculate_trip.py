#!/usr/bin/env python3

#imports
import json
import math

#global variables
mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """Calculate the great-circle distance between two points on a sphere.
    
    Arguments:
        latitude_1 (float): Latitude of the first point in degrees.
        longitude_1 (float): Longitude of the first point in degrees.
        latitude_2 (float): Latitude of the second point in degrees.
        longitude_2 (float): Longitude of the second point in degrees.
        
    Returns:
        float: Great-circle distance between the two points in kilometers.
    """
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def calc_timeTravel(speed: float, distance: float) -> float:
    """Calculate the time required to travel a given distance at a given speed.
    
    Arguments:
        speed (float): Travel speed in km/hr.
        distance (float): Distance to be traveled in km.
        
    Returns:
        float: Time required to travel the distance in hours.
    """
    timeTravel = distance / speed
    return timeTravel

def calc_timeSample(key_string: str, sample_time_dict: dict) -> int:
    """Get the time required to sample a site, given its composition type.
    
    Arguments:
        key_string (str): Composition type of the site.
        sample_time_dict (dict): Dictionary mapping composition types to sampling times.
        
    Returns:
        int: Time required to sample the site in hours.
    """
    timeSample = sample_time_dict[key_string]
    return timeSample

def main():
    """Main function of the program. Loads data from a JSON file, calculates travel times and sampling times,
    and outputs the results.
    """
    with open("sites.json", 'r') as inFile:
        siteDict = json.load(inFile)
    sites = siteDict["sites"]

    dict_sampleTime = {"stony": 1, "iron": 2, "stony-iron": 3}
    SPEED = 10 #km/hr
    latitude = 16.0
    longitude = 82.0
    timeTotal = 0.0
    numLegs = 0
    for site in sites:
        distance = calc_gcd(latitude, longitude, site["latitude"], site["longitude"])
        latitude = site["latitude"]
        longitude = site["longitude"]
        timeTravel = calc_timeTravel(SPEED, distance)
        timeSample = calc_timeSample(site["composition"], dict_sampleTime)
        timeTotal += timeTravel + timeSample
        numLegs += 1
        print(f'leg = {numLegs}, time to travel = {timeTravel} hr, time to sample = {timeSample} hr')

    print("===============================")
    print(f'number of legs = {numLegs}, total time elapsed = {timeTotal} hr')
        
#call to main function
if __name__ == '__main__':
    main()
    
