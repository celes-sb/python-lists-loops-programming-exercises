
coordinatesList = [
    [33.747252,-112.633853],
    [-33.867886, -63.987],
    [41.303921, -81.901693],
    [-33.350534, -71.653268]]

# Your code go here:
longitude = []

for coord in coordinatesList:
    long = coord[1]  # Extract the longitude from the inner list
    longitude.append(long)

for long in longitude:
    print(long)