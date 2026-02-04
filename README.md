# Advanced Electron Microscopy & Diffraction

## Project Structure & Data Setup

This repository contains analysis notebooks and outputs for MATSCI 465 assignments.

Due to GitHub's file size limits (>100MB), the raw 4D-STEM datasets (e.g., `.dm4` files) are excluded from this repository via `.gitignore`. You must download the raw data separately and place them in the `raw_data/` folder for the notebooks to run.

### Expected Directory Tree

```text
.
├── assignment_01_setup.ipynb         # Week 01: Basic Stats & Intro
├── assignment_02_setup.ipynb         # Week 02: 4D-STEM & Virtual Detectors
├── raw_data/                         # <--- PLACE YOUR RAW DATA HERE
│   ├── Si-SiGe.dm4                   # (Required for Assignment 02)
│   ├── Diffraction SI_Au_Calib.dm4   # (Required for Calibration)
│   └── example_EM_Image.tif          # (Required for Assignment 01)
├── assignment_01_output/             # Generated outputs for Week 01
├── assignment_02_output/             # Generated outputs for Week 02
│   ├── figures/                      # Saved plots (BF, ADF, Profiles)
│   └── data/                         # Processed intermediate data
├── README.md
└── .gitignore

```

> **Action Required:** > Before running the notebooks, verify that `Si-SiGe.dm4` and other raw files are located inside the `raw_data/` directory.

---

## Environment Details & Installation

The analysis is performed in a dedicated Conda environment named `matsci465`.

**Python Version:** 3.11+

**Key Libraries:** `py4DSTEM`, `HyperSpy`, `NumPy`, `Matplotlib`, `JupyterLab`

### Quick Start

To reproduce the environment, run the following commands in your terminal:

1. **Create and activate the environment:**

```bash
conda create -n matsci465 python=3.11 -y
conda activate matsci465

```

2. **Install required packages:**

```bash
conda install -c conda-forge jupyterlab numpy scipy matplotlib hyperspy py4dstem -y

```

3. **Launch Jupyter Lab:**

```bash
jupyter lab

```

---

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
