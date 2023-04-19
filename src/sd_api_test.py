from elsapy.elssearch import ElsSearch
from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
from urllib.parse import quote_plus as url_encode
import json, pathlib


def sd():
    ## Load configuration
    con_file = open("config.json")
    config = json.load(con_file)
    con_file.close()

    ## Initialize client
    client = ElsClient(config['apikey'])
    client.inst_token = config['insttoken']

    ## Author example
    # Initialize author with uri
    my_auth = ElsAuthor(
        uri='https://api.elsevier.com/content/author/author_id/7004367821')
    # Read author data, then write to disk
    if my_auth.read(client):
        print("my_auth.full_name: ", my_auth.full_name)
        my_auth.write()
    else:
        print("Read author failed.")

    # my_query = 'prism:publicationName(Computers and Geosciences)'
    # my_search = ElsSearch(my_query, api_key)
    # my_search.execute()
    # print(my_search.results)
    # OUTPUT: A list of dictionaries containing metadata of articles


if __name__ == "__main__":
    sd()
