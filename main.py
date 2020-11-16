import json
import random

def main():
    # Initializing and Declaring Variables
    jsonData = []
    cityarr = ['Franklin, TX', 'Cleveland, TX', 'Normangee, TX', 'Midway, TX', 
    'Groveton, TX', 'North Zulch, TX', 'Madisonville, TX', 'Bedias, TX', 
    'Snook, TX', 'Navasota, TX', 'Dodge, TX', 'Riverside, TX', 'Onalaska, TX', 
    'Coldspring, TX', 'Willis, TX', 'Huntsville, TX', 'College Station, TX', 
    'Bryan, TX', 'Roans Prairie, TX', 'Anderson, TX']

    citylat = [31.02610, 30.491211, 31.032810, 31.02602, 31.054907, 30.91769,
    30.949911, 30.775749, 30.488816, 30.387985, 30.745469, 30.852966, 30.805746,
    30.592421, 30.424928, 30.723526, 30.627977, 30.674364, 30.584366, 30.487697]

    citylon = [-96.486053, -94.994904, -96.115082, -95.750503, -95.125769, 
    -96.108291, -95.911619, -95.949397, -96.46441, -96.087735, -95.397997, -95.403552, 
    -95.116325, -95.129382, -95.479942, -95.550777, -96.334407, -96.369963, -95.943842, 
    -95.992451]

    # Loops 10,000 times to get a lot of data
    for i in range(10000):
        # Gets a random number between all the possible latitudes
        # Grabs the closest one, to what is given
        lat = closest(citylat, random.uniform(30.491211, 31.026810))

        # Gives a random number of Covid Cases
        cc = random.uniform(100, 5000) * .0001

        # Grabs the city based on the relative closest city via Latitude
        city_choice = cityarr[citylat.index(lat)]

        #Grabs the Longitude based on the relative closest city via Latitude
        lon = citylon[citylat.index(lat)]

        # Multiplies Latitude and Longitude to give more realistic data
        lat = lat*random.uniform(1, 1.000345)
        lon = lon*random.uniform(1, 1.000345)

        # Bias for Covid Cases
        if city_choice == 'Huntsville, TX'  or city_choice == 'College Station, TX' or city_choice == "Bryan, TX":
            cc = random.uniform(5000, 10000) * .001
        elif city_choice == 'Franklin, TX' or city_choice == 'Cleveland, TX' or city_choice == 'Normangee, TX':
            cc = random.uniform(0, 2000) * .0001

        # Adds some Noise to the map
        if i % 50 == 0:
            lat = random.uniform(30.491211, 31.026810)
            lon = random.uniform(-96.486053, -94.994904)
            cc = random.uniform(1, 15)
            city_choice = 'No_City'

        data = {
            'lat' : lat,
            'lng' : lon,
            'confirmed_cases' : cc, 
            'city' : city_choice
        }
        jsonData.append(data)



    with open('confirmed_covid.json', 'w') as outfile:
        json.dump(jsonData, outfile)

#Gets the closest value to the given number
def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 

if __name__ == "__main__":
    main()
