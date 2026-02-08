import hashlib
import json
import time

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = None  # Initially None, set after mining/hashing

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        Excludes the 'hash' field itself to ensure consistency.
        """
        # Create a copy of the dict to not modify the object state
        block_data = self.__dict__.copy()
        
        # Remove hash if it exists to avoid circular dependency or incorrect hashing
        if 'hash' in block_data:
            del block_data['hash']
            
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, [], "0")
        # For genesis, we just compute hash. Nonce is 0.
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * 2) and
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * 2):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

class SecureBlockchain(Blockchain):
    def check_chain_validity(self):
        result = {
            'is_valid': True,
            'details': []
        }
        # Start from 1 because genesis block (0) is special
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            # 1. Check if current hash is consistent with data
            # When we verify, we MUST calculate the hash of the *current data*
            # and compare it to the *stored hash*.
            recalculated_hash = current.compute_hash()
            
            if current.hash != recalculated_hash:
                result['is_valid'] = False
                result['details'].append(f"Block {i}: Data tampering detected! Stored hash {current.hash} != Calculated {recalculated_hash}")
            
            # 2. Check if previous hash matches
            if current.previous_hash != previous.hash:
                result['is_valid'] = False
                result['details'].append(f"Block {i}: Broken link! Previous hash {current.previous_hash} != {previous.hash}")
                
        return result
