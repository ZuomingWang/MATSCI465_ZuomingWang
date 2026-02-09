# Advanced Electron Microscopy & Diffraction

<<<<<<< HEAD

## Project Structure & Data Setup

This repository contains analysis notebooks and outputs for MATSCI 465 assignments.

=======
-------

## Project Structure & Data Setup

This repository contains analysis notebooks and outputs for MATSCI 465 assignments.

>>>>>>> f259358eb (Add README, Assignment 4 notebook, raw_data, and output folder)
>>>>>>> Due to GitHub's file size limits (>100MB), the raw 4D-STEM datasets (e.g., `.dm4` files) are excluded from this repository via `.gitignore`. You must download the raw data separately and place them in the `raw_data/` folder for the notebooks to run.
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>

### Expected Directory Tree

```text
.
├── assignment_01_setup.ipynb         # Week 01: Basic Stats & Intro
├── assignment_02_setup.ipynb         # Week 02: 4D-STEM & Virtual Detectors
<<<<<<< HEAD
├── raw_data/                         # <--- PLACE YOUR RAW DATA HERE
│   ├── Si-SiGe.dm4                   # (Required for Assignment 02)
│   ├── Diffraction SI_Au_Calib.dm4   # (Required for Calibration)
│   └── example_EM_Image.tif          # (Required for Assignment 01)
├── assignment_01_output/             # Generated outputs for Week 01
├── assignment_02_output/             # Generated outputs for Week 02
│   ├── figures/                      # Saved plots (BF, ADF, Profiles)
│   └── data/                         # Processed intermediate data
=======
├── assignment_04_combined.ipynb      # Week 04: Nanoparticle Analysis (Classical, ML, DL)
├── raw_data/                         # <--- PLACE YOUR RAW DATA HERE
│   ├── Si-SiGe.dm4                   # (Required for Assignment 02)
│   ├── Diffraction SI_Au_Calib.dm4   # (Required for Calibration)
│   ├── example_EM_Image.tif          # (Required for Assignment 01)
│   └── 11500X*.png                   # (Required for Assignment 04 DOPAD)
├── assignment_01_output/             # Generated outputs for Week 01
├── assignment_02_output/             # Generated outputs for Week 02
├── assignment_04_output/             # Generated outputs for Week 04
│   ├── data/
│   │   ├── deep_learning/        # Generated datasets (Task 3)
│   │   │   ├── cnn/              # Image crops for classification
│   │   │   │   ├── train/        # (Classes 0/1)
│   │   │   │   └── val/          # (Classes 0/1)
│   │   │   └── unet/             # Full images/masks for segmentation
│   │   ├── processed/            # CSV results (classical_results, ml_results)
│   │   └── raw/                  # Copied raw images
│   └── figures/                  # Saved plots (final_panel.png)
>>>>>>> f259358eb (Add README, Assignment 4 notebook, raw_data, and output folder)
├── README.md
└── .gitignore

```

> **Action Required:** > Before running the notebooks, verify that `Si-SiGe.dm4` and other raw files are located inside the `raw_data/` directory.

---

## Environment Details & Installation

The analysis is performed in a dedicated Conda environment named `matsci465`.

**Python Version:** 3.11+

<<<<<<< HEAD
**Key Libraries:** `py4DSTEM`, `HyperSpy`, `NumPy`, `Matplotlib`, `JupyterLab`
=======================

**Key Libraries:** `py4DSTEM`, `HyperSpy`, `NumPy`, `Matplotlib`, `JupyterLab`, `scikit-image`, `scikit-learn`, `tensorflow`

>>>>>>> f259358eb (Add README, Assignment 4 notebook, raw_data, and output folder)
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>

### Quick Start

To reproduce the environment, run the following commands in your terminal:

1. **Create and activate the environment:**

```bash
conda create -n matsci465 python=3.11 -y
conda activate matsci465

```

2. **Install required packages:**

```bash
<<<<<<< HEAD
conda install -c conda-forge jupyterlab numpy scipy matplotlib hyperspy py4dstem -y
=======
conda install -c conda-forge jupyterlab numpy scipy matplotlib hyperspy py4dstem scikit-image scikit-learn -y
pip install tensorflow
>>>>>>> f259358eb (Add README, Assignment 4 notebook, raw_data, and output folder)

```

3. **Launch Jupyter Lab:**

```bash
jupyter lab

```

---

<<<<<<< HEAD
============

## Assignment 04: Nanoparticle Detection Pipeline

This module implements and compares three distinct approaches for detecting and analyzing nanoparticles in TEM images.

### Methodology

1. **Classical Image Analysis (Task 1)**

   * **Technique:** Noise reduction (Median Filter), contrast enhancement (CLAHE), Otsu thresholding, Distance Transform, and Watershed segmentation.
   * **Pros:** Fast, explainable, no training data needed.
   * **Cons:** Sensitive to noise, fixed parameters (requires tuning for different conditions).
2. **Machine Learning (Task 2)**

   * **Technique:** Extracted morphological and intensity features (Area, Perimeter, Mean Intensity, etc.) from segmented regions.
   * **Models:** K-Means clustering (unsupervised classification) to identify groups, followed by SVM and Random Forest (supervised) to classify particles.
   * **Outcome:** Successfully classified particle populations with high accuracy (>98%).
3. **Deep Learning (Task 3)**

   * **Technique:** End-to-end learning from pixel data (using masks generated by the Classical pipeline as ground truth).
   * **CNN (Classification):** A custom 2-block CNN trained to classify individual particle crops.
   * **U-Net (Segmentation):** A fully convolutional network trained to perform binary segmentation.
   * **Pros:** Robust to noise, learns complex features, no manual feature engineering necessary.
   * **Cons:** Requires labeled data, computationally expensive.

### Quantitative Comparison (Observed Results)

| Method                  | Task           | Metric (F1 / Dice) | Notes                                            |
| :---------------------- | :------------- | :----------------- | :----------------------------------------------- |
| **Watershed**     | Segmentation   | N/A                | Baseline for shape extraction                    |
| **SVM**           | Classification | ~0.98              | Linear separation on features                    |
| **Random Forest** | Classification | 1.00               | Feature-based, prone to overfitting if not tuned |
| **CNN**           | Classification | ~0.90              | Learned from 64x64 pixel crops                   |
| **U-Net**         | Segmentation   | ~0.83 (Dice)       | Pixel-wise segmentation accuracy                 |

### Recommendations

* **Use Classical Methods** for rapid prototyping or simple, high-contrast images where speed is critical.
* **Use Random Forest** when you have a good set of extracted features and tabular data; it showed perfect separation on this dataset.
* **Use Deep Learning (U-Net)** for complex segmentation tasks where simple thresholding fails, though it requires more computation and training data.

---

>>>>>>> f259358eb (Add README, Assignment 4 notebook, raw_data, and output folder)
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>

## Assignment 02: 4D-STEM & Virtual Detectors

### Virtual Detectors Concept

One of the most powerful features of 4D-STEM is the ability to perform **"virtual imaging"** post-acquisition.

Unlike conventional STEM, where physical detectors (like Bright Field or Annular Dark Field) are fixed in hardware during the experiment, 4D-STEM records the full 2D diffraction pattern at every scan position.

This allows us to "replay" the experiment in software by defining virtual detectors:

* **Method:** By creating digital masks (e.g., circular, annular, or custom shapes) on the diffraction plane, we can integrate the signal falling onto these specific regions.
* **Advantage:** We can generate BF, ADF, or other contrast modes from the exact same dataset long after the microscope session is finished. This allows us to optimize the detector geometry for the specific features of interest without needing to rescan the sample.

### Key Outputs

* **Virtual BF & ADF Images:** Reconstructed from the Si/SiGe interface dataset using the Python pipeline.
* **Diffraction Analysis:** Center of Mass (CoM) calculation and radial intensity profiling (calibrated to  or mrad).

---

## Assignment 01: Introduction & Statistics

### Content

* **assignment_01_setup.ipynb**: The main Jupyter Notebook where environment verification, data loading, and basic statistical analysis (mean, standard deviation, histograms) are performed.
* **Analysis:** Statistical processing of `example_EM_Image.tif`.
