import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# Dictionary to store blockchain data
blockchain = {}

# Function to add a block to the blockchain
def add_block_to_chain(block):
    blockchain[block.block_hash] = block.block_data

# Function to retrieve and print transaction history by navigating backward through the hashes
def traverse_blockchain(starting_hash):
    current_hash = starting_hash
    while current_hash in blockchain:
        transaction_history = blockchain[current_hash]
        print(f"\nTransaction History for Hash '{current_hash}':\n{transaction_history}")
        
        # Find the previous block hash (the last part of the transaction history after the last hyphen)
        previous_block_hash = transaction_history.split("-")[-1]
        
        if previous_block_hash == "Initial String":  # Reached the initial block
            print("\nReached the last known transaction.")
            break
        
        current_hash = previous_block_hash

# Create transactions and blocks
t1 = "$50,000 sent to Green Cotton Farms Co. for 20,000 lbs of organic cotton."
t2 = "$20,000 sent to local harvesters for ethically handpicking cotton."
t3 = "$15,000 sent to EcoSpin Mills for eco-friendly cotton yarn"
t4 = "$25,000 sent to Green Loom Factory for fabric production using solar power"
t5 = "$18,000 sent to EarthDye Solutions for natural dyeing of fabrics."
t6 = "$40,000 sent to FairWear Factory for 5,000 t-shirts with ethical labor."
t7 = "$2,500 sent to EcoPack Co. for biodegradable packaging."
t8 = "$7,000 sent to GreenShip Logistics for low-emission shipping by sea."
t9 = "$5,000 sent to EcoMarket Ltd. for distribution via carbon-neutral channels."
t10 = "$1,000 invested in eco-friendly garment care education."
t11 = "$2,000 sent to RecycleGreen Co. for garment recycling programs."
t12 = "$250 sent by User to GreenBrand Store for purchasing 1 sustainable T-shirt."

# Create and add blocks to the blockchain
initial_block = NeuralCoinBlock("Initial String", [t1, t2])
add_block_to_chain(initial_block)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])
add_block_to_chain(second_block)

third_block = NeuralCoinBlock(second_block.block_hash, [t4, t5])
add_block_to_chain(third_block)

fourth_block = NeuralCoinBlock(third_block.block_hash, [t5, t6])
add_block_to_chain(fourth_block)

fifth_block = NeuralCoinBlock(fourth_block.block_hash, [t6, t7])
add_block_to_chain(fifth_block)

sixth_block = NeuralCoinBlock(fifth_block.block_hash, [t7, t8])
add_block_to_chain(sixth_block)

seventh_block = NeuralCoinBlock(sixth_block.block_hash, [t8, t9])
add_block_to_chain(seventh_block)

eighth_block = NeuralCoinBlock(seventh_block.block_hash, [t9, t10])
add_block_to_chain(eighth_block)

ninth_block = NeuralCoinBlock(eighth_block.block_hash, [t10, t11])
add_block_to_chain(ninth_block)

tenth_block = NeuralCoinBlock(ninth_block.block_hash, [t11, t12])
add_block_to_chain(tenth_block)

# Provide the user with the last block's hash
last_block_hash = tenth_block.block_hash
print(f"The last block's hash is: {last_block_hash}")

# Ask the user for the starting hash to traverse the blockchain
user_hash = input("\nEnter the last block hash to start traversing (or type 'exit' to quit): ")

if user_hash != 'exit':
    traverse_blockchain(user_hash)

