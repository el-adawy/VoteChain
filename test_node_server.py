from node_server import app, blockchain
from flask import json
import pytest



def test_1():
    cpt = 0
    response = app.test_client().post(
        '/submit',
        data = json.dumps({'author' : 'Paul', 'content' : 'Joe Biden'}),
        content_type = 'application/json',
        )
    response = app.test_client().post(
        '/submit',
        data = json.dumps({'author' : 'Paul', 'content' : 'Emmanuel Macron'}),
        content_type = 'application/json',
        )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200

    for elt in blockchain.chain:
        for tx in blockchain.transactions:
            if (tx['author'] == 'Paul'):
                cpt++
    assert cpt == 1
    #tester si y a un seul vote de Paul en parcourant la blockchain
    


def test_2():
    cpt = 0
    response = app.test_client().post(
        '/submit',
        data = json.dumps({'author' : 'Paul', 'content' : 'Joe Biden'}),
        content_type = 'application/json',
        )
    response = app.test_client().get(
        '/mine'
        )
    response = app.test_client().post(
        '/submit',
        data = json.dumps({'author' : 'Paul', 'content' : 'Emmanuel Macron'}),
        content_type = 'application/json',
        )
    response = app.test_client().get(
        '/mine'
        )
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    
        for elt in blockchain.chain:
        for tx in blockchain.transactions:
            if (tx['author'] == 'Paul'):
                cpt++
                
    assert cpt == 1
    #tester si y a un seul vote de Paul en parcourant la blockchain
