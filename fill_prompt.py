import sys
import langchain
from load_chunks import load_chunks
from prompts import GRAPH_EXTRACTION_PROMPT, CLAIM_EXTRACTION_PROMPT



def fill_graph_extraction_prompt():
    template = langchain.PromptTemplate(template=GRAPH_EXTRACTION_PROMPT)

    tuple_delimiter = "<|>"
    record_delimiter = "##"
    completion_delimiter = "<|COMPLETE|>"
    entity_types = "CHARACTERS, LOCATIONS, SPELLS, EVENTS"
    input_text = "".join(load_chunks(20, 10))

    formatted = template.format(tuple_delimiter=tuple_delimiter, record_delimiter=record_delimiter, completion_delimiter=completion_delimiter, entity_types=entity_types, input_text=input_text)

    #save the formatted text to a file
    with open("prompt.txt", "w") as f:
        f.write(formatted)

def fill_claim_extraction_prompt():
    template = langchain.PromptTemplate(template=CLAIM_EXTRACTION_PROMPT)

    tuple_delimiter = "<|>"
    record_delimiter = "##"
    completion_delimiter = "<|COMPLETE|>"
    input_text = "".join(load_chunks(20, 10))
    claim_description = "Any claims or facts that could be relevant to information discovery."
    entity_specs = "CHARACTERS, LOCATIONS, SPELLS, EVENTS"

    formatted = template.format(tuple_delimiter=tuple_delimiter, record_delimiter=record_delimiter, completion_delimiter=completion_delimiter, input_text=input_text, claim_description=claim_description, entity_specs=entity_specs)

    #save the formatted text to a file
    with open("prompt.txt", "w") as f:
        f.write(formatted)


if __name__ == "__main__":
    # parameters

    if len(sys.argv) < 1:
        print("Add the type of prompt you want to generate")
        sys.exit(1)

    type = sys.argv[1]

    if type == "CLAIM_EXTRACTION_PROMPT":
        fill_claim_extraction_prompt()
    elif type == "GRAPH_EXTRACTION_PROMPT":
        fill_graph_extraction_prompt()
