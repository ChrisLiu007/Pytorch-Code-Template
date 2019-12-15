# Experiment the test
# Dataset: sample
# imagesize: 256x128
# batchsize: 16x4
python3 tests/dataset_test.py --config_file='configs/baseline.yml' \
                            MODEL.DEVICE_ID "('1')" \
                            DATASETS.NAMES "('sample')" \
                            DATASETS.ROOT_DIR "('../data')" \
                            MODEL.PRETRAIN_CHOICE "('self')" \
                            TEST.WEIGHT "('../model')"