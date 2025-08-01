"""
Train DeepCAD RT on OABF dataset

Usage: srun --mem=24G --gres=gpu:3 --time=00:30:00 --partition=boost_usr_prod --qos=boost_qos_dbg python depcad_train.py

OOM: `select_img_num` and `train_datasets_size` only affect RAM requirement, not VRAM
"""

from deepcad.train_collection import training_class
from deepcad.movie_display import display
from deepcad.utils import get_first_filename, download_demo
from pathlib import Path

training_class(
    {
        "patch_x": 150,  # the width of 3D patches
        "patch_y": 150,  # the height of 3D patches
        "patch_t": 150,  # the time dimension (frames) of 3D patches
        "overlap_factor": 0.4,  # overlap factor
        "scale_factor": 1,  # the factor for image intensity scaling
        "select_img_num": 6000,  # select the number of frames used for training (use all frames by default)
        "train_datasets_size": 5000,  # datasets size for training (how many 3D patches)
        "datasets_path": "../dataset/sample/motion_corrected/resonant_neuro",  # folder containing files for training
        "pth_dir": "./pth",  # the path for pth file and result images
        # network related parameters
        "n_epochs": 20,  # the number of training epochs
        "lr": 0.00005,  # learning rate
        "b1": 0.5,  # Adam: bata1
        "b2": 0.999,  # Adam: bata2
        "fmap": 16,  # model complexity
        "GPU": "0",  # GPU index
        "num_workers": 0,  # if you use Windows system, set this to 0.
        "visualize_images_per_epoch": False,  # whether to show result images after each epoch
        "save_test_images_per_epoch": True,  # whether to save result images after each epoch
        "UNet_type": "ResidualUNet3D",
    }
).run()
