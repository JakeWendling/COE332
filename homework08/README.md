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
By default, this app automatically pulls the prebuilt Docker Image from Docker Hub to run the Flask app.

### Building a Docker image using the Dockerfile
To build your own image, you will need to create a [Docker Hub](https://hub.docker.com/) account and push your own Docker Image.

1. First modify the .yml files in this folder by replacing all instances of "jakew57" with your own username.
2. Change the name of all the "jakew57...yml" files from "jakew57-..." to "<username>-..."
3. Enter the following to build the container using the Dockerfile contained in this repository:
```
docker build . -t <docker_hub_username>/gene_app:hw07
```
4. In the "...-flask-deployment.yml" file, change the image from "jakewendling/gene_app:hw07" to your docker image name: "<docker_hub_username>/gene_app:hw07"
5. Once the Docker Image is created, enter the following command to upload it to docker hub for the service to use.
```
docker push
```
6. In the gene_api.py file, in the "get_redis_client" function, change host="jakew57-test-redis-service" to your username: host="<username>-test-redis-service"
7. In all future steps, use your username instead of "jakew57"

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
kubectl apply -f jakew57-test-flask-deployment.yml
kubectl apply -f jakew57-test-redis-deployment.yml
kubectl apply -f jakew57-test-redis-pvc.yml
kubectl apply -f python-debug-deployment.yml
```

This starts two kubernetes services, one for the Flask application, and one for the Redis database.
When running this for the first time, it will take a few minutes to download the data. Once this is done, the following commands will work.

### Requesting Data
Requesting data requires the user to enter a terminal inside a kubernetes pod.

To enter the pod:
```bash
kubectl exec -it -f python-debug-deployment.yml -- /bin/bash
```

You should now see something like the following:
```bash
root@python-debug-deployment-5486696bcd-l6887:/#
```

Now you can run the following commands:

### Commands

To load the data into the app, run the following:
```
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

When you are finished with this application you can exit the pod:
```
exit
```

To turn off the application, enter the following:
```bash
kubectl delete service jakew57-test-flask-service
kubectl delete service jakew57-test-redis-service
kubectl delete deployment jakew57-test-flask-deployment
kubectl delete deployment jakew57-test-redis-deployment
kubectl delete deployment py-debug-deployment
```

To remove the data storage:
```
kubectl delete pvc jakew57-test-redis-pvc
```