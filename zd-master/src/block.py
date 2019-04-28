import hashlib
import datetime as date



class Block:
	#type: 1 Produced, 2 Split, 3 Transfered, 4 Sold
	def __init__(self, id, item, f_location, quantity, owner, date_produced, condition, previous_block):
		#block data
		self.id = id
		self.item = item
		self.f_location = f_location
		self.void = False
		self.quantity = quantity
		self.owner = owner
		self.date_produced = date_produced
		self.condition = condition
		#meta data
		if(previous_block == None):
			self.index = 0
		else:
			self.index = previous_block.index + 1

		self.timestamp = date.datetime.now()
		#previous block metadata
		if(previous_block == None):
			self.previous_hash = None
		else:
			self.previous_hash = previous_block.hash
		self.hash = self.hash_block()

	def hash_block(self):
		sha = hashlib.sha256()
		sha.update(str(self.item).encode('utf-8') + str(self.f_location).encode('utf-8') + str(self.void).encode('utf-8') + str(self.quantity).encode('utf-8') +
		str(self.owner).encode('utf-8') + str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') +
		str(self.previous_hash).encode('utf-8'))
		return sha.hexdigest()
