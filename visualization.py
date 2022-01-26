import glob
import json
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

from utils import get_data


def viz(ground_truth, predictions):
    """
    create a grid visualization of images with color coded bboxes
    args:
    - ground_truth [list[dict]]: ground truth data
    """
    
    # IMPLEMENT THIS FUNCTION     
    paths = glob.glob('data/images/*')
    # mapping to access data faster
    gtdic = {}
    for gt in ground_truth:
        gtdic[gt['filename']] = gt

    pred_dic = {}
    for pred in predictions:
        pred_dic[pred['filename']] = pred

    # color mapping of classes
    colormap = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}        
    pred_color = [1,1,0]

    f, ax = plt.subplots(4, 5, figsize=(20, 10))
    for i in range(20):
        x = i % 4
        y = i % 5
        filename = os.path.basename(paths[i])
        img = Image.open(paths[i])
        ax[x, y].imshow(img)

        bboxes = gtdic[filename]['boxes']
        classes = gtdic[filename]['classes']

        # Draw ground truth
        for cl, bb in zip(classes, bboxes):
            y1, x1, y2, x2 = bb
            rec = patches.Rectangle((x1, y1), x2- x1, y2-y1, facecolor='none',  edgecolor=colormap[cl])
            ax[x, y].add_patch(rec)

        # Draw prediction
        if filename in pred_dic:
            bboxes = pred_dic[filename]['boxes']
            classes = pred_dic[filename]['classes']            
            for cl, bb in zip(classes, bboxes):
                y1, x1, y2, x2 = bb
                rec = patches.Rectangle((x1, y1), x2- x1, y2-y1, facecolor='none',  edgecolor=pred_color)
                ax[x, y].add_patch(rec)

        ax[x ,y].axis('off')
        
    plt.tight_layout()
    plt.show()

if __name__ == "__main__": 
    ground_truth, predictions = get_data()
    print(predictions)
    viz(ground_truth, predictions)