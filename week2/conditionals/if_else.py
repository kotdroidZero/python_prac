# Branching
# else if in Python is elif

def hintUserName(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 character long")
    elif len(username)>15:    
        print("Invalid username. Must be at most 15 character long")
    else:
        print("Valid username")

hintUserName("465")  

"aa".strip()

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = (filesize//block_size)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (block_size*full_blocks) + block_size
    return block_size*full_blocks

print(calculate_storage(1))







