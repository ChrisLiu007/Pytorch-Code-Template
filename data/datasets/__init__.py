"""
This is the dataset read initial file
for read different dataset based on the
dataset name.
"""

# read the image dataset for loader
from .loader import ImageDataset
# read the sample dataset, will output all 
# the list of training and validation
from .sample import Sample

__author__ = ""

# We need define the datasets and 
# using the name of configure to
# local the dataset, we used in this 
# configure.
__factory = {
    'sample': Sample,

}

# This is using the factory to local
# the special dataset by name as key.
def init_dataset(name, *args, **kwargs):
    if name not in __factory.keys():
        raise KeyError("Unknown datasets: {}".format(name))
    return __factory[name](*args, **kwargs)
