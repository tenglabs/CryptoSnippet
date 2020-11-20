import hashlib
from block import Block
blockchain = []

genesis_block = Block("Message", ['Someone Sent Something', '5 btc sent to Satoshi', 'Sample Data'])

second_block = Block(genesis_block.block_hash, ['Curious Data'])

third_block = Block(second_block.block_hash, ['Curious Data Number Two'])



print('First Block Hash:',genesis_block.block_hash)

print('Second Block Hash:',second_block.block_hash)

print('Third Block Hash:',third_block.block_hash)




#hash = hashlib.sha256('secret message'.encode()).hexdigest()
#print(hash)