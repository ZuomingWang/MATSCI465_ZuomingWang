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
