# Homework 07: Gene Data App Service

The Human Genome Organization (HUGO) is a non-profit which oversees the HUGO Gene Nomenclature Committee (HGNC). 

This Flask application is used for querying, storing, and returning information from the HGNC Gene data set. 

The data used in this program can be found at [this link](https://www.genenames.org/download/archive/). This data is found in an json file and contains a dictionary of data for thousands of different genes. It contains data such as, gene symbols, names, aliases, families, and more. An extended description of the data can be found in the above link.

## Installation

Install this project by cloning the repository and creating a folder to store data:

```bash
git clone https://github.com/JakeWendling/COE332.git
cd COE332
cd homework07
```

## Creating the Docker Container
You have the option of using a prebuilt container, or creating your own.

### Using the Prebuilt Container
By default, this app automatically pulls the prebuilt Docker Image to run the Flask app.

### Building a Docker image using the Dockerfile
Enter the following to build the container using the Dockerfile contained in this repository:

```bash
docker build . -t jakewendling/gene_app:hw07
```

## Running the Code

This code has several functions:
1. Return the entire data set in dictionary format.
2. Return a list of the genes availble.
3. Return a dictionary of gene data for a specific gene.

To perform these functions:

### Starting the Flask app and the Redis Database
First start both applications by adding their services to kubernetes:

```bash
kubectl apply -f jakew57-test-redis-service.yml
kubectl apply -f jakew57-test-flask-service.yml
```

This starts two containers, one for the Flask application, and one for the Redis database.
When running this for the first time, it will take a few minutes to download the data. Once this is done, the following commands will work.

### Requesting Data
Requesting data requires the user to enter a terminal inside a kubernetes pod.

To enter the pod:
```bash
kubectl exec -it -f jakew57-test-flask-deployment.yml -- /bin/bash
```

You should now see something like the following:
```bash
root@jakew57-test-flask-deployment-5486696bcd-l6887:/#
```

To exit the pod:
```
exit
```

Now you can run the following commands:

### Commands

To load the data into the app, run the following:
```bash
curl -X POST jakew57-test-flask-service:5000/data
```

To delete the data from the app, run the following
```bash
curl -X DELETE jakew57-test-flask-service:5000/data
```

Doing this will cause all of the other requesting routes to fail.

#### To request the entire dataset:
```bash
curl jakew57-test-flask-service:5000/data
```

#### To request the list of genes:
```bash
curl jakew57-test-flask-service:5000/genes
```
This will return something similar to the following:
```bash
["HGNC:2341","HGNC:5",...
```

#### To request the data for a specific gene:
(you can copy one of the genes given in the previous command)
```
curl jakew57-test-flask-service:5000/genes/<gene>
```

Example usage:
```bash
curl jakew57-test-flask-service:5000/genes/"HGNC:5"
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
kubectl delete service jakew57-test-flask-service
kubectl delete service jakew57-test-redis-service
```