# This is a sample of deep learning structure in pytorch


## 1. Introduction
```
1. config: 
    - defaults.py : is the basic configuration
    - baseline.yml : is one of the chanagable
2. data:
    dataset :
        - loader.py : is call the torchvision
        - sample.py : special dataset for extractive of name list.
    samplers :
        - build.py : how to return a idx of dataset loader.
    transorms :
        - build.py : transforms build.
    - build.py : return the training dataset and validate dataset.
3. engine
    call the iginite in pytorch
4. layers
    define the loss 
5. modeling
    include the backones 
6. solver
    for the learning rate schedule and load weight 
7. tools
    setup the train or test
```

## Reference
```
https://github.com/michuanhaohao/reid-strong-baseline
```

## License

[MIT](LICENSE) © Sohone Guo