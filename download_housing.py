import os
from pathlib import Path
import tarfile
from six.moves import urllib
import pandas as pd


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = Path(__file__).parent
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")

    urllib.request.urlretrieve(housing_url, tgz_path)

    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

    os.remove('housing.tgz')

class loud_housing():
    def __init__(self, housing = HOUSING_PATH):
        self.housing = housing.joinpath('housing.csv')
        self.csv_path = pd.read_csv(self.housing, sep=',', header=None)

    def array(self,):
        return pd.read_csv(self.housing, sep=',', header=None, skiprows=1).to_numpy()



