from node_server import blockchain
import requests
import pytest


def test_vote():
	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Paul', 'content': 'Joe Biden'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:8000/mine'
	response = requests.get(url)
	assert response.status_code == 200

def test_1():
	cpt = 0
	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Paul', 'content': 'Joe Biden'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:5000/submit'
	myobj = {'author': 'Paul', 'content': 'Emmanuel Macron'}
	response = requests.post(url, data = myobj)
	assert response.status_code == 200

	url = 'http://localhost:8000/mine'
	response = requests.get(url)
	assert response.status_code == 200
        
        #vérification
	for elt in blockchain.chain:
		for tx in elt.transactions:
			print(tx)
			if (tx['author'] == 'Paul'):
				cpt+=1

	assert cpt == 1
    
'''

def test_2():
	cpt = 0
	headers = {
    'Content-type': 'application/json',
}
	data = "{'author' : 'Paul', 'content' : 'Joe Biden'}"
	response = requests.post(
            'http://localhost:5000/submit',
                headers = headers,
            data = data
        )
	response = requests.get(
        'http://localhost:8000/mine'
        )
	response = requests.post(
            'http://localhost:5000/submit',
                headers = headers,
            data = data
        )
	response = requests.get(
        'http://localhost:8000/mine'
        )



	assert response.status_code == 200

	for elt in blockchain.chain:
		for tx in elt.transactions:
			if (tx['author'] == 'Paul'):
				cpt+=1

	assert cpt == 1
    #tester si y a un seul vote de Paul en parcourant la blockchain
'''
