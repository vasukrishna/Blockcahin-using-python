from block import Block        

class Blockchain:
    
    """
    Blokchain is a  public ledger  of transactions.
    Implemented as a  list of blocks - data sets of transactions 
    """

    def __init__(self):
        self.chain = []

    def add_block(self,data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain:{self.chain}'

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
blockchain.add_block('vasu')

print(blockchain)
