'''
    Muhammad Nur Yasir Utomo (yasirutomo@gmail.com)
'''

# reference: https://eatsleepdata.com/data-viz/how-to-generate-a-geographical-heatmap-with-python.html
# Import the necessary libraries
import pandas as pd
import gmplot
# For improved table display in the notebook
from IPython.display import display

raw_data = pd.read_csv("geotagged/stream_sampleoutputstream.csv")

# Success! Display the first 5 rows of the dataset
# display(raw_data.head(n=5))
# display(raw_data.info())

# Let's limit the dataset to the first 15,000 records for this example
# data = raw_data.head(n=25000)
data = raw_data

# Store our latitude and longitude
latitudes = data["lat"]
longitudes = data["lng"]

# Creating the location we would like to initialize the focus on.
# Parameters: Lattitude, Longitude, Zoom
gmap = gmplot.GoogleMapPlotter(-6.2757858,106.1902966, 5)

# Overlay our datapoints onto the map
gmap.heatmap(latitudes, longitudes)

# Generate the heatmap into an HTML file
gmap.draw("my_heatmapoutput.html")