import json

def compute_average_mass(a_list_of_dicts, a_key_string):
    total_mass = 0.0
    for d in a_list_of_dicts:
        total_mass += float(d[a_key_string])
    return (total_mass / len(a_list_of_dicts))

def check_hemisphere(latitude: float, longitude: float) -> str:    # type hints
    location = ''
    if (latitude > 0):
        location = 'Northern'
    else:
        location = 'Southern'
    if (longitude > 0):
        location = f'{location} & Eastern'
    else:
        location = f'{location} & Western'
    return(location)

def countTypes(dictList, key):
    typeFreq = {}
    for d in dictList:
        typeValue = d[key]
        if typeValue in typeFreq:
            typeFreq[typeValue] += 1
        else:
            typeFreq[typeValue] = 1
    return typeFreq

def main():
    with open('Meteorite_Landings.json', 'r') as inFile:
        data = json.load(inFile)

    typeFreq = countTypes(data['meteorite_landings'], 'recclass')
    for d in typeFreq.items():
        print(f'{d[0]}, {d[1]}')

    #print(compute_average_mass(data['meteorite_landings'], 'mass (g)'))

    #for row in data['meteorite_landings']:
    #    print(check_hemisphere(float(row['reclat']), float(row['reclong'])))

if __name__ == '__main__':
    main()
