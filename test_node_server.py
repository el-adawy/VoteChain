from node_server import blockchain
from flask import json
import requests
import pytest


def test_vote():
	cpt = 0
	cpt2= 0
	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Paul', 'content': 'Joe Biden'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:8000/mine'
	response = requests.get(url)
	assert response.status_code == 200

        #vérification
	url = 'http://localhost:8000/chain'
	response = requests.get(url)
	assert response.status_code == 200


	response_dict = json.loads(response.text)
	for elt in response_dict['chain']:
		print(elt['transactions'])
		if (elt != []):
			print(elt['transactions'])
			for elt2 in elt['transactions']:
				if( elt2['author'] == 'Paul' ):
					cpt += 1
				if ( elt2['content'] == 'Joe Biden'):
					cpt2=1
	assert cpt == 1
	assert cpt2 == 1
	
def test_1():
	cpt = 0
	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Jack', 'content': 'Joe Biden'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Jack', 'content': 'Emmanuel Macron'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:8000/mine'
	response = requests.get(url)
	assert response.status_code == 200
        
        #vérification
	url = 'http://localhost:8000/chain'
	response = requests.get(url)
	assert response.status_code == 200


	response_dict = json.loads(response.text)
	for elt in response_dict['chain']:
    		print(elt['transactions'])
    		if (elt != []):
        		print(elt['transactions'])
        		for elt2 in elt['transactions']:
            			if( elt2['author'] == 'Jack' ):
                                    cpt+=1
	assert cpt == 1
  

def test_2():
	cpt = 0
	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Olaf', 'content': 'Joe Biden'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:8000/mine'
	response = requests.get(url)
	assert response.status_code == 200

	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Olaf', 'content': 'Emmanuel Macron'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:8000/mine'
	response = requests.get(url)
	assert response.status_code == 200
        
        #vérification
	url = 'http://localhost:8000/chain'
	response = requests.get(url)
	assert response.status_code == 200

	response_dict = json.loads(response.text)
	for elt in response_dict['chain']:
    		print(elt['transactions'])
    		if (elt != []):
        		print(elt['transactions'])
        		for elt2 in elt['transactions']:
            			if( elt2['author'] == 'Jack' ):
                                    cpt+=1
	assert cpt == 1
