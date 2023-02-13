# Homework 03: Turbidity Testing

Scenario: Your robot has finished collecting its five meteorite samples and has taken them back to the Mars lab for analysis. In order to analyze the samples, however, you need clean water. You must check the latest water quality data to assess whether it is safe to analyze samples, or if the Mars lab should go on a boil water notice.

The data used in this program can be found at [this link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json). This data contains a dictionary of water samples that contain the date and time, sample volume, calibration constant, detector current, and the name of the person who analyzed the sample.

## Installation

Install this project by cloning the repository, making the scripts executable
For example:

```bash
git clone git@github.com:JakeWendlingUT/COE332.git
cd COE332
cd homework03
chmod u+x analyze_water.py
```

## Running the Code

This code has three functions:
1. Get the turbidity data from a given url
2. Calculate the average turbidity of the last five samples and inform the user whether the water is clean
3. Inform the user how long it will take for the turbidity to reduce to accepted levels

To perform these functions:

```bash
./analyze_water.py
```

This should print something similar to the following:
```
Average turbidity based on most recent five measurements = 1.155868 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.169909191009603 hours
```
This shows the average turbidity of the last five samples (sorted by time sampled), whether the water is safe to use, and the minimum time required for the water to become safe.