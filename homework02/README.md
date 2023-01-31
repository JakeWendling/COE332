# Homework 02: Mars Meteor Site Generator

Scenario: You are operating a robotic vehicle on Mars and the task for today is to investigate five meteorite landing sites in Syrtis Major.

This purpose of this project is to generate random meteor sites on mars and calculate the amount of time a rover would take to collect samples from said sites.


## Installation

Install this project by cloning the repository, making the scripts executable
For example:

```bash
git clone git@github.com:JakeWendlingUT/COE332.git
cd homework02
chmod u+x calculate_trip.py
chmod u+x generate_sites.py
```

## Running the Code

This code has two functions:
1. Generate random meteor sites and save them in sites.json
2. Read in meteor sites from sites.json and calculate the time it would take for a robot to travel to each site and collect samples

To generate the sites.json file run the following:

```bash
./generate_sites.py
```

To read in meteor sites:

```bash
./calculate_trip.py
```

This should print something similar to the following:
```bash
leg = 1, time to travel = 11.75 hr, time to sample = 1 hr
leg = 2, time to travel = 3.43 hr, time to sample = 2 hr
leg = 3, time to travel = 4.53 hr, time to sample = 1 hr
leg = 4, time to travel = 6.04 hr, time to sample = 2 hr
leg = 5, time to travel = 10.43 hr, time to sample = 3 hr
===============================
number of legs = 5, total time elapsed = 45.17 hr
```
This shows how long the robot took to get to each site, how long it takes to collect samples depending on the type of meteor, and the total amount of time the robot took on its mission. 