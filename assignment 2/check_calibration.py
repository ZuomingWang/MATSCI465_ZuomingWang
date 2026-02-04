
import py4DSTEM
import numpy as np

try:
    file_path = "assignment_02_output/data/raw/Si-SiGe.dm4"
    dataset = py4DSTEM.import_file(file_path)
    print("Dataset loaded.")
    
    if hasattr(dataset, 'calibration'):
        cal = dataset.calibration
        print("Calibration object attributes:")
        print(dir(cal))
        
        # Try to find diffraction pixel size
        vals = []
        if hasattr(cal, 'diffraction_pixel_size'):
            vals.append(f"diffraction_pixel_size: {cal.diffraction_pixel_size}")
        if hasattr(cal, 'qx_scale'):
            vals.append(f"qx_scale: {cal.qx_scale}")
        if hasattr(cal, 'scale'):
            vals.append(f"scale: {cal.scale}")
            
        print("Found values:", vals)
        
except Exception as e:
    print(f"Error: {e}")
