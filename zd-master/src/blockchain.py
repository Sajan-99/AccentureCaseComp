from block import Block
import random

class Blockchain:

	def __init__(self):

		self.comp_array = []
		#self.add_genesis(item, f_location, quantity, owner)
		return

	def last_block(self):
		return self.comp_array[-1]

	def print_last_block(self):
		block = self.comp_array[-1]
		print("block id is " + str(block.id))
		return

	def check_integrity(self):
		curr = self.last.block()
		#to be written
		return

	def add_genesis(self, genesis):
		self.comp_array.append(genesis)
		print("item added")
		#self.comp_array[0] = genesis
		return

	def add_block(self, new_block):
		if(self.last_block().timestamp > new_block.timestamp):
			print("New block occured earlier")
			return
		if(len(self.comp_array) == 0):
			print("Not genesis block")
			return
		self.comp_array.append(new_block)
		print("item added")
		return

	def check_traits(self, id):
		block = self.last_block()
		index = block.index
		print("index of last block is " + str(index))
		found = False

		while(found == False and index >= 0):
			block = self.comp_array[index]
			print("current block id is " + str(block.id))
			if(block.id == id):
				print("found item")
				found = True
				item = block.item
				f_location = block.f_location
				quantity = block.quantity
				void = block.void
				owner = block.owner
				date_produced = block.date_produced
				condition = block.condition
				date_shipped = block.timestamp
			else:
				index = index - 1
		if(index == 0 and found == False):
			print("item not found")
			return None
		return [item, f_location, quantity, void, owner, date_produced, condition, date_shipped]

	#to consumer
	def void_item(self, id):
		item, f_location, quantity, void, owner, date_produced, condition, date_shipped = self.check_traits(id)
		new_block = Block(id, item, f_location, quantity, owner, date_produced, condition, self.last_block())
		new_block.void = True
		self.add_block(new_block)
		return

	def transfer_item(self, id, new_owner):
		item, f_location, quantity, void, owner, date_produced, condition, date_shipped = self.check_traits(id)
		new_block = Block(id, item, f_location, quantity, owner, date_produced, condition, self.last_block())
		new_block.owner = new_owner
		self.add_block(new_block)
		return

	def split_item(self, id, quantity):
		item = self.check_traits(id)
		if(item.quantity <= quantity):
			print("Insufficient quantity, cannot split")
			return Blockchain
		self.void(id)
		old_item = Block(item.item, item.f_location, item.quantity - quantity, item.owner, item.date_produced, item.condition, self.last_block())
		self.add_block(old_item)
		new_item = Block(item.item, item.f_location, quantity, item.owner, item.date_produced, item.condition, self.last_block())
		self.add_block(new_item)
		return Blockchain
