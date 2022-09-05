import flask
from flask import Flask, request
import json
import re
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/conv": {"origins": "*"}})


############################################
#                                          #
#      TO DO: Fill Out app.route Args      #
#                                          #
############################################
@app.route("/conv", methods=['POST']) ## Line to fill out.
def conversation_analysis():
    '''
    This function is completed for you
    Input:
        There is no input to this function
    Output:
        The longest two unique sentences in the conversation
    '''
    conversation = request.form.get('conversation') # Get conversation
    # See if the request is valid
    if conversation is None:
        flask.abort(400, description="Missing conversation")

    # Check convo length
    if len(conversation) > 3000:
        flask.abort(400, description="The conversation is too long")
    
    # Get the sentences from the conversation
    sentences = get_sentences(conversation)
    
    # Identify the longest two sentences
    max_sentences = {'sentences': longest_sentences(sentences)}
    print(max_sentences)
    return json.dumps(max_sentences)


@app.route("/", methods=['GET'])
def index():
    '''This function is completed for you as the base endpoint'''
    return "Server is live!"


def get_sentences(conversation: str) -> list:
    '''
    This function is completed for you
    Input:
        conversation: string containing the conversation from the api request
    Output:
        A list of the sentences in the conversation

    '''
    #Replace the unnecessary person tags with sentence breaks
    conversation = re.sub(r"#.*#:\s*", r"||", conversation)
    
    # Create a list of sentences
    sentences = [sen.strip() for sen in conversation.split(r"||")]
    return sentences

def longest_sentences(sents: list) -> list:
    '''
    Input:
        sents: A list of the sentences returned from get_sentences
    Ouput:
        A list of length two of the two longest unique sentences with
        the longest being in position 0 and the second longest in 
        position 1
    '''
    # find the first longest one in the list, remove it
    # find the second longest one in the list
    # return result
    rst = []
    
    firstLong = max(sents, key = len)
    
    sents.remove(firstLong)
    
    secondLong = max(sents, key=len)
    
    # append two result together
    rst.append(firstLong)
    rst.append(secondLong)
    
    return rst

if __name__ == "__main__":
    app.run()