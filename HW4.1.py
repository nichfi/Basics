# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:44:35 2023

@author: nicko
"""
import csv

def dms_format(degrees):
    """Converts decimal degrees to degrees, minutes, and seconds."""
    direction = "N" if degrees >= 0 else "S"
    degrees = abs(degrees)
    minutes, seconds = divmod(degrees * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    degree_str = f"{int(abs(degrees))}°{int(minutes)}'{seconds:.2f}\" {direction}"    
    return degree_str

def dms_formatE(degrees):
    """Converts decimal degrees to degrees, minutes, and seconds."""
    direction2 = "E" if degrees >= 0 else "W"
    degrees = abs(degrees)
    minutes, seconds = divmod(degrees * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    degree_str = f"{int(abs(degrees))}°{int(minutes)}'{seconds:.2f}\" {direction2}"    
    return degree_str

def main():
    while True:
        
        # Prompt user for input CSV file name
        print("Enter the name of the file to be read:")
        filename = input()
        try:
            # Open input CSV file
            with open(filename, newline='') as csvfile:
                break
        except:
            print("Error in reading the file '{}'. Please try again.".format(filename))
    print('File read successfully.')
    print('Conversions are as follows:')
    with open(filename, newline='') as csvfile:          
        reader = csv.reader(csvfile)            
        next(reader)
        cities = [(row[0], float(row[1]), float(row[2])) for row in reader]
    # Convert latitude and longitude to DMS format using dms_format() function
    latitudes_dms = list(map(dms_format, [city[1] for city in cities]))
    longitudes_dms = list(map(dms_formatE, [city[2] for city in cities]))

    # Combine city names, latitudes, and longitudes using zip()
    data = list(zip([city[0] for city in cities], latitudes_dms, longitudes_dms))

    # Iterate through data and print the final results
    for city, lat, lon in data:
       
        print("{}: {}, {}".format(city, lat, lon))


            
main()