import xmltodict
import requests
from typing import List
from flask import Flask, request

app = Flask(__name__)
data = None

@app.route('/data', methods=['POST'])
def postData() -> dict:
    """
    Gets the HGNC data and saves the data in dictionary format in the flask app.

    Returns:
        string: Message that tells the user that the data has successfuly been obtained
    """
    response = requests.get('https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
    global data
    data = xmltodict.parse(response.text)
    return "Data reloaded\n"

@app.route('/data', methods=['DELETE'])
def deleteData() -> str:
    """
    Deletes the data stored in the flask app

    Returns:
        string: success message
    """
    global data
    data = None
    return "Data deleted\n"

@app.route('/data', methods=['GET'])
def getData() -> dict:
    """
    Gets the HGNC data and returns the data in dictionary format

    Returns:
        data: The stored data in dictionary format.
    """
    global data
    if not data:
        return "Data not found\n", 400
    return data

@app.route('/genes', methods=['GET'])
def getGenes() -> List[str]:
    """
    Gets the HGNC data and returns the list of genes in a list
    
    Returns:
        idList: a list of id's of genes(strings) for which gene data is available.
    """
    global data
    if not data:
        return "Data not found\n", 400
    geneList = data['respsonse']['docs']

    idList = []
    for gene in geneList:
        idList.append(geneList['hgnc_ids'])
    return idList

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
    global data
    if not data:
        return "Data not found\n", 400
    geneList = data['respsonse']['docs']
    for state in stateList:
        if gene['hgnc_id'] == hgnc_id:
            return gene
    return "Error: Gene not found\n", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
