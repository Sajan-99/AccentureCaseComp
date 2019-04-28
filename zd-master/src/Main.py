from blockchain import Blockchain

from block import Block

import requests
from flask import Flask, jsonify, url_for, request, redirect, render_template

app = Flask(__name__)


egg = Blockchain()

genesis = Block(1, "Pre-packed Strawberries", "Leppington NSW", 400, "Woolworths", "10/03/2019", "Good", None)

egg.add_genesis(genesis)

block2 = Block(2, "OMG Organic Milk 1 Litre", "Mydena Tas", 200, "Woolworths", "4/3/2019", "Bad - E.Coli Recall", egg.last_block())

egg.add_block(block2)

block3 = Block(3, "Fresh Farm Eggs 12-pack", "Rossmore NSW", 500, "Coles", "2/4/2019", "Bad - Salmonella Recall", egg.last_block())

egg.add_block(block3)

data = egg.check_traits(1)


data = egg.check_traits(2)
egg.transfer_item(2, "big boi")


data = egg.check_traits(3)
egg.void_item(2)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/barcode', methods=['POST'])
def barcode():
	barcode = request.form['barcode']
	id = int(barcode,10)
	data = egg.check_traits(id)
	if data is None:
		return render_template('index.html', notfound="Not found!")

	return render_template('barcode.html',id=barcode,
		item=data[0],
		source_location=data[1],
		quantity=data[2],
		sold=data[3],
		owner=data[4],
		date_produced=data[5],
		condition=data[6],
		date_shipped=data[7]
	)


if __name__ == '__main__':
    app.run(debug=True)
