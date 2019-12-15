"""
This is a example how to make a function 
for the dataset loader.
"""

import glob
import os.path as osp
import re

__author__ = ""

class Sample():

    def __init__(self, root='', **kwargs):
        super(Sample, self).__init__()
        
        """
        This is the dataset handler
        1. We need declare the path 
           of dataset.
           e.g. folder = osp.join(root, self.dataset_dir)
                train = osp.join(folder, 'train')
                val = osp.join(folder, 'val')
                
        2. We need checkout whether the 
           folder existed or etc.
           e.g. if not osp.exists(path):
                raise RuntimeError("'{}' is not available".format(self.dir))
                
        3. We need collected the dataset
           as list. 
           e.g. [1.jpg, 2.jpg,...]
                image = glob.glob(osp.join(path, '*.jpg'))
                re.compile(r'([-\d]+)_c(\d)').search(img_path).groups()
                
        4. We need declare the dataset 
           information, for example, 
           the num of image of training
           and validata.
           
        """
        pass

    def _check_before_run(self):
        pass

    def _process_dir(self, path):
        pass
