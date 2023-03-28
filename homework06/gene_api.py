import requests
import redis
import json
from typing import List
from flask import Flask, request

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)

@app.route('/data', methods=['POST'])
def postData() -> dict:
    """
    Gets the HGNC data and saves the data in dictionary format in the flask app.

    Returns:
        string: Message that tells the user that the data has successfuly been obtained
    """
    response = requests.get('https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    rd = get_redis_client()
    data = response.json()
    geneList = data['response']['docs']
    
    for gene in geneList:
        rd.hset('data', gene['hgnc_id'], json.dumps(gene))
    return "Data loaded\n"

@app.route('/data', methods=['DELETE'])
def deleteData() -> str:
    """
    Deletes the data stored in the redis db

    Returns:
        string: success message
    """
    
    rd = get_redis_client()
    rd.flushall()
    return "Data deleted\n"

@app.route('/data', methods=['GET'])
def getData() -> dict:
    """
    Gets the HGNC data and returns the data in dictionary format

    Returns:
        data: The stored data in dictionary format.
    """
    rd = get_redis_client()
    data = []
    for key in rd.hgetall('data'):
        data.append(json.loads(rd.hget('data', key)))
    #if data == "":
    #    return "Data not found\n", 400
    return data

@app.route('/genes', methods=['GET'])
def getGenes() -> List[str]:
    """
    Gets the HGNC data and returns the list of genes in a list
    
    Returns:
        idList: a list of id's of genes(strings) for which gene data is available.
    """
    #if not data:
    #    return "Data not found\n", 400
    #geneList = data['response']['docs']
    rd = get_redis_client()
    return rd.hkeys('data')

@app.route('/genes/<hgnc_id>', methods=['GET'])
def getGene(hgnc_id: str) -> dict:
    """
    Gets the HGNC data, 
    then returns the gene data for a given HGNC ID, if available. 
    Otherwise returns an error message and error code.
    
    Args:
        hgnc_id: A string representing a gene's HGNC ID.
        
    Returns:
        geneData: Dictionary containing data about the given gene, if available. 
    
    Raises:
        If no gene data is available for the given gene id, 
        returns an error message and a 400 status code.
    """
    rd = get_redis_client()
    for key in rd.hgetall('data'):
        gene = json.loads(rd.hget('data', key))
        if gene['hgnc_id'] == hgnc_id:
            return gene
    return "Error: Gene not found\n", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
