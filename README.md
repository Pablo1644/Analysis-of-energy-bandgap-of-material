# Energy Bandgap Calculation from Transmission Measurements

This repository contains a Python script designed to calculate the energy bandgap of materials using the Tauc-plot method. The script processes transmission measurement data from multiple files and performs a series of computations to determine the bandgap energy.
## Description

## The script follows these steps:
<b>1. Initialization:</b>
        Defines the thickness of the sample (d).
        Retrieves the current working directory and lists all .txt files present in the directory. </br>
<b>2. Data Loading and Preparation:</b>
        Reads the first file into a Pandas DataFrame, skipping the first row and setting column names to ['λ[nm]', 'TRANSMISSION'].
        Iteratively reads the rest of the files, summing their transmission values. </br>
<b>3. Averaging Transmission Values:</b>
        Calculates the average transmission by dividing the summed transmission values by the number of files. </br>
<b>4. Plotting Transmission vs. Wavelength:</b>
        Plots the average transmission against the wavelength using Matplotlib. </br>
<b>5. Calculating Absorption Coefficient (α):</b>
        Computes the absorption coefficient for each wavelength.
        Converts wavelengths to energies. </br>
<b>6. Tauc Plot Calculation:</b>
        Computes αhν^1/2 values and plots them against energies. </br>
<b>7. Fitting a Linear Curve:</b>
        Selects energy values in a specified range (3.97 to 4.762 eV) for fitting a linear curve.
        Uses NumPy's polyfit to fit the linear curve to the selected data points.
        Calculates the energy bandgap from the linear fit. </br>
<b>8. Plotting the Fitted Curve:</b>
        Plots the fitted curve on the Tauc plot to visually determine the energy bandgap.
        Prints the calculated bandgap energy. </br>

## Requirements

    Python 3.x
    numpy
    pandas
    matplotlib
    os
    fnmatch
    math


## Notes
    Adjust the energy range for the linear fit as necessary by modifying the energies_for_fit and alpha_hv_for_fit selection criteria.
    Ensure the files are correctly formatted and located in the same directory as the script for proper execution.

