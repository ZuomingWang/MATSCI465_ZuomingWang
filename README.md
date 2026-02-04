# MATSCI465_ZuomingWang

## Repository Contents

- **assignment_01_setup.ipynb**: The main Jupyter Notebook where environment verification, data loading, and basic statistical analysis (mean, standard deviation, histograms) are performed.
- **example_EM_Image.tif**: The sample electron microscopy dataset used for the analysis.

## Environment Details

The analysis is performed in a dedicated Conda environment named `matsci465`.

**Python Version:** 3.11+

### Key Libraries

The following core packages are used:

- **Jupyter Lab**: For interactive coding and visualization.
- **NumPy & SciPy**: For numerical computation and scientific analysis.
- **Matplotlib**: For plotting and data visualization.
- **HyperSpy**: For multidimensional data analysis, specifically tailored for microscopy.
- **py4DSTEM**: For 4D scanning transmission electron microscopy data analysis.

## Setup Instructions

To reproduce the environment, run the following commands in your terminal:

1. **Create the environment:**

   ```bash
   conda create -n matsci465 python=3.11 -y
   ```
2. **Activate the environment:**

   ```bash
   conda activate matsci465
   ```
3. **Install the required packages:**

   ```bash
   conda install -c conda-forge jupyterlab numpy scipy matplotlib hyperspy py4dstem -y
   ```
4. **Launch Jupyter Lab:**

   ```bash
   jupyter lab
   ```

## Assignment 02: 4D-STEM & Virtual Detectors

### Virtual Detectors Concept

One of the most powerful features of 4D-STEM is the ability to perform "virtual imaging" post-acquisition. Unlike conventional STEM, where physical detectors (like BF or ADF) are fixed in hardware during the experiment, 4D-STEM records the full 2D diffraction pattern at every scan position.

This allows us to "replay" the experiment in software by defining virtual detectors. By creating digital masks (e.g., circular, annular, or custom shapes) on the diffraction plane, we can integrate the signal falling onto these specific regions to reconstruct images. This means we can generate Bright Field (BF), Annular Dark Field (ADF), or other contrast modes from the exact same dataset long after the microscope session is finished, essentially optimizing the detector geometry for the specific features of interest without needing to rescan the sample.
