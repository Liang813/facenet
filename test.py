import tensorflow as tf
import sys
import os
import subprocess

interpreter_path = sys.executable
print("Running at: ", interpreter_path)

assert tf.__version__ == "1.8.0"


def get_target_dir():
    for x in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if version in x:
            return x
    raise ValueError("No dir ends with %s!" % version)


'''
bug can be reproduced when image_num could be divided by image_batch
'''
subprocess.call(
    [interpreter_path, "./%s/contributed/export_embeddings.py" % get_target_dir(), "--image_batch=10", "./model",
     "./data"])
