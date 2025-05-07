# Dataset Class
#- This class encapsulate the info associated to the path of each dataset od interest

from enum import Enum

class Dataset(Enum):
    DEATH_VALLEY = "datasets/death_valley_2021_simple.csv"
    SITKA_JULY = "datasets/sitka_weather_07-2021_simple.csv"
    SITKA_2021 = "datasets/sitka_weather_2021_simple.csv"