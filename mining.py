import hashlib

def mine_block(previous_hash, block_number, transactions):
    
    nonce = 0
    while True:
        # Exact format matching the Word table
        block_data = f"""Previous_Hash:{previous_hash} Block_Number:{block_number} Transactions:{transactions} Nonce:{nonce}"""
        
        # Compute SHA-256 hash
        block_hash = hashlib.sha256(block_data.encode(encoding="utf-8")).hexdigest()
        
        # Check if hash starts with '0'
        if block_hash.startswith("0"):
            print(f"✅ Block {block_number} Mined!")
            print(f"Hash: {block_hash}")
            print(f"Nonce: {nonce}")
            return nonce, block_hash, block_data

        # Increment nonce and try again
        nonce += 1

# Example mining for Block N
previous_hash = "32612036"
block_number = "N"
transactions = {  "N":"97aa:(J:10->A:9.9); 2450:(H:5,H:10->B:4.8,D:10)",
                
                "N+1":"3ab1:(A:9.9->C:6,A:3.7); 464f:(J:10->D:3,C:6.8)",
                
                "N+2":"7e18:(C:6.8->X:6.5); 391d:(A:3.7->C:2,A:1.5)",
                
                "N+3":"f9d8:(J:6.8->C:4,B:2.5); fcc5:(D:10->C:4.8,B:5)",
                
                "N+4":"c50b:(B:5->D:1.5,B:3.2); af51:(C:6,C:2->A:7,C:0.8)",
                
                "N+5":"824f:(X:6.7,X:10->B:6.6,D:9.9); 47a9:(A:7->J:6.6)",
                
                "N+6":"fa09:(D:3,D:9.9->A:9.5,D:3); 4106:(B:2.5,B:3.2,B:6.6->A:11.9)"}

nonce, valid_hash, block_data = mine_block(previous_hash, block_number, transactions)

# Print result for Word table entry
print("Exact Block Data:")
print(block_data)