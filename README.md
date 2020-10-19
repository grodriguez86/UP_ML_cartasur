# Universidad de Palermo | Machine Learning | Cartasur

## CHANGELOG

### 2020-10-18

Abandoned `work.py` in favor of a better organization of the code. Basically now we need to have files that reflect what they're doing since we're going to analyze the data using different algorithms and ways. So I am splitting the files based on different algorithms and moving the common structure (such as data manipulation and data correction) to a single library.

Additions:

- **`kmeans.py`**: Analisys using kmeans

- **`lib/load_data.py`**: Bunch of functions to load the data and present it in a proper way.

