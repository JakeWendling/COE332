import json

#def 

def main():
    latitude = 16.0
    longitude = 82.0
    SPEED = 10 #km/hr
    MARS_R = 3389.5 #km
    with open("sites.json", 'r') as inFile:
        siteDict = json.load(inFile)
    sites = siteDict["sites"]

    timeTaken = 0.0
    numLegs = 0
    for site in sites:
        print(site["site_id"])

if __name__ == "__main__":
    main()
