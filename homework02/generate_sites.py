#!/usr/bin/env python3

import json
import random as r

def generateSite(id_num: int) -> dict:
    """
    Generates a site with random latitude, longitude, and composition.
    
    Parameters:
    id_num (int): The id number for the site.
    
    Returns:
    dict: A dictionary with keys "site_id", "latitude", "longitude", and "composition".
    """
    latitude = r.uniform(16.0, 18.0)
    longitude = r.uniform(82.0, 84.0)
    composition_types = ["stony", "iron", "stony-iron"]
    composition = composition_types[r.randint(0,2)]
    dict_site = {"site_id": id_num,
                  "latitude": latitude,
                  "longitude": longitude,
                  "composition": composition
                  }
    return dict_site

def main():
    """
    Generates 5 sites with random latitude, longitude, and composition and writes them to a JSON file.
    """
    sites = []
    for i in range(1,6):
        sites.append(generateSite(i))
    siteDict = {"sites": sites}
    with open("sites.json", 'w') as outFile:
        json.dump(siteDict, outFile)

if __name__ == "__main__":
    main()

