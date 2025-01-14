import requests

# Replace with your Google Maps API Key
GOOGLE_MAPS_API_KEY = 'AIzaSyB3HojfiI-5nEUrTmp7C439Q8c6lt5MSck'

def get_google_maps_data(location):
    google_maps_url = f'https://maps.googleapis.com/maps/api/geocode/json'
    
    params = {
        'address': location,
        'key': GOOGLE_MAPS_API_KEY
    }
    
    # Send the request to the Google Maps API
    response = requests.get(google_maps_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if the location was found
        if data['results']:
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            formatted_address = data['results'][0]['formatted_address']
            
            print(f"Location: {formatted_address}")
            print(f"Latitude: {lat}, Longitude: {lng}")
            
            # Generate Google Static Map URL (example of a map)
            map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=600x400&key={GOOGLE_MAPS_API_KEY}'
            print(f"Map URL: {map_url}")
        else:
            print("Location not found.")
    else:
        print("Error fetching Google Maps data.")

def main():
    # Get location input from the user
    location = input("Enter a location (city/landmark): ")
    
    # Fetch Google Maps data (coordinates and static map) for the location
    get_google_maps_data(location)

if __name__ == "__main__":
    main()
