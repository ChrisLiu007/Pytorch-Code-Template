
import os.path as osp

from PIL import Image
from torch.utils.data import Dataset

__author__ = ""

def read_image(image_dir):
    """Read the image
    
    e.g. img = Image.open(img_path).convert('RGB')
    
    Arguments:
        image_dir {[type]} -- [description]
    """
    pass


class ImageDataset(Dataset):
    """[summary]
    
    Arguments:
        Dataset {[type]} -- [description]
    """
    def __init__(self):
        pass

    def __len__(self):
        # Return the length of dataset
        pass
    
    def __getitem__(self, index):
        """Read the image base on the indexs
        Using the transform and augmentation
        
        Arguments:
            index {[type]} -- [description]
        """
        pass
