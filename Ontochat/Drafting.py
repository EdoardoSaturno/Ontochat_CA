import json
from ontochat.chatbot import chat_completion
from io import StringIO
import os
import sys

key = "s" #put your openAI key here !!!!!
key = str(key)

def rdf_explanations(message):

    print("Current Directory:", current_dir)  #Please ensure this path is connected to your onrochat folder
    sys.path.append(current_dir)

    # Get the current working directory
    current_dir = r"S" #please provide tha path to the directory of ontochat !!!!!

    t1_dir = r"\Tests\Test1.txt"
    t2_dir = r"\Tests\Test2.txt"
    t3_dir = r"\Tests\Test3.txt"



    # Obtain the message that describe the ontology, either "t" for test or input your own description
    if message=="Test1":
        with open(current_dir + t1_dir, 'r') as file:
            message = file.read()
    
    if message=="Test2":
        with open(current_dir + t2_dir, 'r') as file:
            message = file.read()

    if message=="Test3":
        with open(current_dir + t2_dir, 'r') as file:
            message = file.read()


    # First block of istr for generating CQ
    instructions = [{
        "role": "system",
        "content": "You are a conversational ontology engineering assistant specialized in RDF generation."
    }, {
        "role": "user",
        "content": "I need you to generate competency questions based on the actual description of the ontology "
    }]

    messages = []
    messages.append({
        "role": "user",
        "content": message
    })

    bot_message = chat_completion(key, instructions + messages)

    #print(bot_message)
    message_turtle = []
    message_xml = []

    message_turtle.append({
        "role": "user",
        "content": bot_message
    })

    message_xml.append({
        "role": "user",
        "content": bot_message
    })

    # Second Block: generate TURTLE text
    instructions_turtle = [{
        "role": "system",
        "content": "You are a conversational ontology engineering assistant specialized in RDF generation."
    }, {
        "role": "user",
        "content": "Here are instructions for you on how to generate high-quality RDF explanations. Start by extracting "
                   "key entities, relationships, and classes from the given ontology competency questions. Next, represent these "
                   "as RDF triples in the format subject-predicate-object. Ensure that the RDF triples accurately reflect "
                   "the ontology's structure and semantics. If the ontology description involves multiple entities or "
                   "relationships, generate RDF triples for each of them. Make sure to use standard RDF vocabularies where "
                   "applicable (e.g., rdfs:Class, rdf:type, owl:ObjectProperty). Make sure to only write the rdf description "
                   "in TURTLE format as a response without comments or other not related text"
    }]

    # Third Block: generate XML text
    instructions_xml = [{
        "role": "system",
        "content": "You are a conversational ontology engineering assistant specialized in RDF generation."
    }, {
        "role": "user",
        "content": "Here are instructions for you on how to generate high-quality RDF explanations. Start by extracting "
                   "key entities, relationships, and classes from the given ontology competency questions. Next, represent these "
                   "as RDF triples in the format subject-predicate-object. Ensure that the RDF triples accurately reflect "
                   "the ontology's structure and semantics. If the ontology description involves multiple entities or "
                   "relationships, generate RDF triples for each of them. Make sure to use standard RDF vocabularies where "
                   "applicable (e.g., rdfs:Class, rdf:type, owl:ObjectProperty). Make sure to only write the rdf description "
                   "in XML format as a response without comments or other not related text"
    }]


    # Final block: get the RDF content generated by the assistant
    bot_message_turtle = chat_completion(key, instructions_turtle + message_turtle)
    bot_message_xml = chat_completion(key, instructions_xml + message_xml)

    return bot_message_turtle, bot_message_xml, bot_message
