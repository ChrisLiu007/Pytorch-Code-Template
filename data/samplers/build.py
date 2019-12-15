import copy
import random
from collections import defaultdict

import numpy as np
import torch
from torch.utils.data.sampler import Sampler

__author__ = ""


class ExampleSampler(Sampler):
    """This is a sampler example
    
    The __iter__ will return a 
    list of dataset, can be sampler
    not speically.
    
    e.g. return iter([0, 1, 2,..])
    
    """

    def __init__(self):
        pass 
    
    def __iter__(self):
        pass

    def __len__(self):
        pass
