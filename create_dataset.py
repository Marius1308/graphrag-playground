import os
from datasets import load_dataset
from langchain.text_splitter import RecursiveCharacterTextSplitter

LOAD_BOOKS = 1
CHUNK_SIZE = 1000
ds = load_dataset("elricwan/HarryPotter", cache_dir="datasets")

text = [ds["train"][i]["content"] for i in range(LOAD_BOOKS)]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap= 0)

chunks = text_splitter.create_documents(text)

#save the chunks to files
for i, chunk in enumerate(chunks):
    os.makedirs(f"datasets/harry_potter_chunks_{CHUNK_SIZE}", exist_ok=True)
    with open(f"datasets/harry_potter_chunks_{CHUNK_SIZE}/hp_{i}.txt", "w") as f:
        f.write(chunk.page_content)
