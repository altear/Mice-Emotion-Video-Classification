'''
Simple script to clean darknet data/train.txt files by removing dead links (ie. training images that were deleted)

This creates a file new-train.txt in the data. To use this, you can manually copy its contents into the data/train.txt file
'''

import sys
import os

os.chdir(sys.argv[1])

with open('data/train.txt', 'r') as fp:
    images = fp.readlines()

images = [image.strip() for image in images]

images = list(filter(lambda x: os.path.exists(x), images))

with open('data/new-train.txt', 'w') as fp:
    fp.write('\n'.join(images))