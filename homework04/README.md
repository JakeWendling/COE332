# Homework 04: ISS Position App

Scenario: You have found an abundance of interesting positional and velocity data for the International Space Station (ISS). It is a challenge, however, to sift through the data manually to find what you are looking for. 

This Flask application is used for querying and returning interesting information from the ISS data set. It returns the most recent position and velocity data of the ISS.

The data used in this program can be found at [this link](https://spotthestation.nasa.gov/trajectory_data.cfm). This data is found in an xml file and contains a dictionary of header data and position/velocity vectors of the ISS every four minutes. It contains the date and time, X, Y, and Z, and X, Y, and Z velocities at each time (epoch).

## Installation

Install this project by cloning the repository, making the scripts executable
For example:

```bash
git clone git@github.com:JakeWendlingUT/COE332.git
cd COE332
cd homework04
chmod u+x iss_tracker.py
```

## Running the Code

This code has three functions:
1. Return the entire data set in dictionary format.
2. Return a list of the epochs/times when positional data of the ISS was taken.
3. Return a dictionary of the position and velocity vectors at a provided epoch.
4. Return the speed of the ISS at a given epoch.

To perform these functions:

### Starting the Flask app
First start the Flask app:
```bash
/coe332/homework04$ flask --app iss_tracker run
```
Then in a separate terminal, you can request the data:

### Requesting Data
#### To request the entire dataset:
```bash
$ curl localhost:5000
```
However, it is recommended to output this data to a file instead of the terminal given its large size:
```bash
$ curl localhost:5000 --output <filename>
```
#### To request the list of epochs:
```bash
$ curl localhost:5000/epochs
```
This will return something similar to the following:
```bash
["2023-048T12:00:00.000Z","2023-048T12:04:00.000Z","2023-048T12:08:00.000Z",...
```
#### To request the positional data for a given epoch:
(you can copy one of the epochs given in the previous command)
```bash
$ curl localhost:5000/epochs/<epoch>
```
Example usage:
```bash
$ curl localhost:5000/epochs/"2023-063T11:59:00.000Z"
{"EPOCH":"2023-063T11:59:00.000Z","X":{"#text":"2511.5681106...
```
This will give the position and velocity vectors of the ISS at the given epoch.

#### To request the speed at a given epoch:
```bash
$ curl localhost:5000/epochs/<epoch>/speed
```
Example usage:
```bash
$ curl localhost:5000/epochs/"2023-063T11:59:00.000Z"/speed
7.662273068417691 km/s
```
