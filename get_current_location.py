import get_current_location
import webbrowser

# Get the current latitude and longitude
g = get_current_location.ip('me')
lat_lng = g.latlng

# Check if lat/lng is fetched successfully
if lat_lng:
    # Open a file in write mode
    with open("iss.txt", "w") as file:
        # Write the latitude and longitude to the file
        file.write("Your current lat / long is: " + str(lat_lng))
    
    # Open the file in the default text editor or browser
    webbrowser.open("iss.txt")
else:
    print("Unable to fetch the current location. Please check your internet connection or try again.")
