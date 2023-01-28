import json
import random as r

def generateSite(id_num: int) -> dict:
    latitude = r.uniform(16.0, 18.0)
    longitude = r.uniform(82.0, 84.0)
    composition_types = ["stony", "iron", "stony-iron"]
    composition = composition_types[r.randint(0,2)]
    dictionary = {"site_id": id_num,
                  "latitude": latitude,
                  "longitude": longitude,
                  "composition": composition
                  }
    return dictionary

def main():
    sites = []
    for i in range(1,6):
        sites.append(generateSite(i))
    siteDict = {"sites": sites}
    with open("sites.json", 'w') as outFile:
        json.dump(siteDict, outFile)
    
if __name__ == "__main__":
    main()
