# encoding: utf-8
"""
@author:  liaoxingyu
@contact: sherlockliao01@gmail.com
"""

import torch
from torch import nn

from .backbones.resnet import ResNet


class Baseline(nn.Module):
    """This is a baseline model
    
    e.g. 
       if model_name == 'resnet18':
            self.in_planes = 512
            self.base = ResNet(last_stride=last_stride, 
                               block=BasicBlock, 
                               layers=[2, 2, 2, 2])
        elif model_name == 'resnet34':
            self.in_planes = 512
            self.base = ResNet(last_stride=last_stride,
                               block=BasicBlock,
                               layers=[3, 4, 6, 3])

    e.g. load the parameter
        def load_param(self, trained_path):
            param_dict = torch.load(trained_path)
            for i in param_dict:
                if 'classifier' in i:
                    continue
                self.state_dict()[i].copy_(param_dict[i])
    Arguments:
        nn {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    def __init__(self):
        super(Baseline, self).__init__()
        pass

    def forward(self, x):
        pass

    def load_param(self):
        pass
