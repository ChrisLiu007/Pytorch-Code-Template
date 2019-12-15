"""
This is collected all the function
and as dataset api.
"""

from torch.utils.data import DataLoader
from .datasets import init_dataset, ImageDataset
from .samplers import ExampleSampler
from .transforms import build_transforms


def make_data_loader(cfg):
    """
    This is to loading the 
    dataset for both training 
    and validate.
    
    1. Declare the trasforms for 
        training or for validate
        e.g. 
        build_transforms(cfg, is_train=True)
        build_transforms(cfg, is_train=False)
    2. Multi-dataset loader
        if len(cfg.DATASETS.NAMES) == 1:
            dataset = init_dataset(cfg.DATASETS.NAMES, 
                                    root=cfg.DATASETS.ROOT_DIR)
        else:
            # TODO: add multi dataset to train
            dataset = init_dataset(cfg.DATASETS.NAMES, 
                                    root=cfg.DATASETS.ROOT_DIR)
    3. Declare the train set. 
        train_set = ImageDataset(dataset.train, train_transforms)
        train_loader = DataLoader(
            train_set, batch_size=batch_size,
            sampler=RandomIdentitySampler(dataset.train, cfg.SOLVER.IMS_PER_BATCH, cfg.DATALOADER.NUM_INSTANCE),
            # sampler=ExampleSampler(dataset.train),
            num_workers=num_workers, collate_fn=train_collate_fn
        )
        def train_collate_fn(batch):
            imgs, pids, _, _, = zip(*batch)
            pids = torch.tensor(pids, dtype=torch.int64)
            return torch.stack(imgs, dim=0), pids
    return training_loader and validate_loader
    
    """
    pass

