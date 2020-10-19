# Universidad de Palermo | Machine Learning | Cartasur

## CHANGELOG

### 2020-10-18

Abandoned `work.py` in favor of a better organization of the code. Basically now we need to have files
that reflect what they're doing since we're going to analyze the data using different algorithms
and ways. So I am splitting the files based on different algorithms and moving the common structure
(such as data manipulation and data correction) to a single library.

Since we're going to use the same dataset but different algorithms it makes sense to have different
files to hold each algorithm separately.

Also we have created a new library called `lib/cartasur` with the following files:

- `lib/cartasur/constants.py`: This is PREVIOUS to use encoders.

- `lib/cartasur/data_loader.py`: This file adds some functionalities to load the files from cartasur and normalize them.

- `lib/cartasur/normalizer.py`: This file have some functions that normalize our data.


Additions:

- **`random_forest.py`**: We added the implementation of the _Random Forest_ algorithm.

- **`kmeans.py`**: We moved some of the code from `work.py` to this file to use the **kmeans** algorithm.

- **`lib/cartasur/`**: We decided to add a library to manage and normalize the dataset from Cartasur.



### PRIOR TO 2020-10-18

- `work.py` we created this file to put our work in here, and created a `./lib/` directory to encapsulate
the libraries functionalities.

