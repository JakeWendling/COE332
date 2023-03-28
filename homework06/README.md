# Homework 06: Gene Data App Container

The Human Genome Organization (HUGO) is a non-profit which oversees the HUGO Gene Nomenclature Committee (HGNC). 

This Flask application is used for querying, storing, and returning information from the HGNC Gene data set. 

The data used in this program can be found at [this link](https://www.genenames.org/download/archive/). This data is found in an json file and contains a dictionary of data for thousands of different genes. It contains data such as, gene symbols, names, aliases, families, and more. An extended description of the data can be found in the above link.

## Installation

Install this project by cloning the repository and creating a folder to store data:

```bash
git clone https://github.com/JakeWendling/COE332.git
cd COE332
cd homework06
mkdir data
```
## Creating the Docker Container
You have the option of using a prebuilt container, or creating your own.

### Using the prebuilt container
Enter the following to pull and run the prebuilt container:
```bash
docker pull jakewendling/gene_app:hw06
```
### Building a Docker image using the Dockerfile
Enter the following to build the container using the Dockerfile contained in this repository:
```bash
docker build . -t jakewendling/gene_app:hw06
```
## Running the Code

This code has several functions:
1. Return the entire data set in dictionary format.
2. Return a list of the genes availble.
3. Return a dictionary of gene data for a specific gene.

To perform these functions:

### Starting the Flask app and the Redis Database
First start both applications using docker-compose:
```bash
docker-compose up -d
```
This starts two containers, one for the Flask application, and one for the Redis database.
When running this for the first time, it will take a few minutes to download the data. Once this is done, the following commands will work.

### Requesting Data
Then, you can request the data.

To load the data into the app, run the following:
```bash
curl -X POST localhost:5000/data
```

To delete the data from the app, run the following
```bash
curl -X DELETE localhost:5000/data
```
Doing this will cause all of the other requesting routes to fail.

#### To request the entire dataset:
```bash
curl localhost:5000/data
```
#### To request the list of genes:
```bash
curl localhost:5000/genes
```
This will return something similar to the following:
```bash
["HGNC:2341","HGNC:5",...
```
#### To request the data for a specific gene:
(you can copy one of the genes given in the previous command)
```bash
curl localhost:5000/genes/<gene>
```
Example usage:
```bash
curl localhost:5000/genes/"HGNC:5"
```
This will give the following:
```bash
{
  "_version_": 1761544680491712512,
    "agr": "HGNC:5",
      "ccds_id": [
          "CCDS12976"
	    ],
	    ...
```

## Turning Off the Application:
To turn off the application enter the following:
```bash
docker-compose stop
```