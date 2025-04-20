import requests
import time

api_key = "ILPWSPI4KO4XA0XT"
"""
amrita_coordinates_set = [
    {"lat": 11.0712, "long": 76.9911},
    {"lat": 11.0673, "long": 76.9881},
    {"lat": 11.0625, "long": 76.9845},
    {"lat": 11.0609, "long": 76.9833},
    {"lat": 11.0569, "long": 76.9803},
    {"lat": 11.0750, "long": 76.9950},
    {"lat": 11.0735, "long": 76.9942},
    {"lat": 11.0700, "long": 76.9905},
    {"lat": 11.0655, "long": 76.9865},
    {"lat": 11.0640, "long": 76.9850},
    {"lat": 11.0630, "long": 76.9830},
    {"lat": 11.0580, "long": 76.9800},
    {"lat": 11.0775, "long": 76.9975},
    {"lat": 11.0760, "long": 76.9960},
    {"lat": 11.0745, "long": 76.9945},
    {"lat": 11.0720, "long": 76.9930},
    {"lat": 11.0695, "long": 76.9915},
    {"lat": 11.0680, "long": 76.9900},
    {"lat": 11.0665, "long": 76.9885},
    {"lat": 11.0650, "long": 76.9870},
    {"lat": 11.0635, "long": 76.9855},
    {"lat": 11.0620, "long": 76.9840},
    {"lat": 11.0610, "long": 76.9820},
    {"lat": 11.0800, "long": 76.9990},
    {"lat": 11.0790, "long": 76.9980},
    {"lat": 11.0780, "long": 76.9970},
    {"lat": 11.0765, "long": 76.9955},
    {"lat": 11.0755, "long": 76.9945},
    {"lat": 11.0740, "long": 76.9930},
    {"lat": 11.0725, "long": 76.9915},
    {"lat": 11.0710, "long": 76.9900}
]
"""
amrita_coordinates_set = [
    {"lat": 11.07121, "long": 76.99111},
    {"lat": 11.07122, "long": 76.99112},
    {"lat": 11.07123, "long": 76.99113},
    {"lat": 11.07124, "long": 76.99114},
    {"lat": 11.07125, "long": 76.99115},
    {"lat": 11.07136, "long": 76.99126},
    {"lat": 11.07137, "long": 76.99127},
    {"lat": 11.07138, "long": 76.99128},
    {"lat": 11.07139, "long": 76.99129},
    {"lat": 11.07140, "long": 76.99130},
    {"lat": 11.07151, "long": 76.99141},
    {"lat": 11.07152, "long": 76.99142},
    {"lat": 11.07153, "long": 76.99143},
    {"lat": 11.07154, "long": 76.99144},
    {"lat": 11.07155, "long": 76.99145},
    {"lat": 11.07166, "long": 76.99156},
    {"lat": 11.07167, "long": 76.99157},
    {"lat": 11.07168, "long": 76.99158},
    {"lat": 11.07169, "long": 76.99159},
    {"lat": 11.07170, "long": 76.99160}
]
def update_thingspeak(lat, long):
    api_endpoint = f"https://api.thingspeak.com/update?api_key={api_key}"
    payload = {"field1": lat, "field2": long}
    response = requests.post(api_endpoint, params=payload)
    if response.status_code == 200:
        print("Upload successful!")
    else:
        print(f"Failed to upload. Status code: {response.status_code}")

if __name__ == "__main__":
    try:
        for coords in amrita_coordinates_set:
            update_thingspeak(coords["lat"], coords["long"])
            time.sleep(15)
    except KeyboardInterrupt:
        print("Script terminated by user.")
