from deepcad.test_collection import testing_class

testing_class(
    {
        "patch_x": 150,  # the width of 3D patches
        "patch_y": 150,  # the height of 3D patches
        "patch_t": 150,  # the time dimension (frames) of 3D patches
        "overlap_factor": 0.6,  # overlap factor,
        "scale_factor": 1,  # the factor for image intensity scaling
        "test_datasize": 500,  # the number of frames to be tested
        "datasets_path": "../dataset/sample/motion_corrected",  # folder containing all files to be tested
        "pth_dir": "./pth",  # pth file root path
        "denoise_model": "motion_corrected_202507301826",  # A folder containing all models to be tested
        "output_dir": "./results",  # result file root path
        # network related parameters
        "fmap": 16,  # number of feature maps
        "GPU": 0,  # GPU index
        "num_workers": 0,  # if you use Windows system, set this to 0.
        "visualize_images_per_epoch": False,  # whether to display inference performance after each epoch
        "save_test_images_per_epoch": True,  # whether to save inference image after each epoch in pth path
    }
).run()
