import os

base_dir= "datasets/harry_potter_chunks_1000"

def load_chunks(start, limit):
    chunks = []
    for i in range(start, start+limit):
        with open(f"{base_dir}/hp_{i}.txt", "r") as f:
            chunks.append(f.read())
    return chunks
