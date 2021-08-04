from types import MethodDescriptorType
from flask import render_template, request, jsonify
from app import app
from app import database

#this is url routing will occur 

# Example:

    # @app.route('/')
    # def example_method(param):

    #     try:
    #         make call to database Methods 
    #         result = ...
    #     except:
    #         result = ...

        
    #     return jsonify(result)


#POST URLs
@app.route("/courses", methods=['POST'])
def ()

@app.route("/professors", methods=['POST'])
def ()

@app.route("/prereqs", methods=['POST'])
def ()

@app.route("/restrictions", methods=['POST'])
def ()


#GET URLs
@app.route("/", methods=['GET'])

#PUT URLs
@app.route("/", methods=['PUT'])


#POST URLs
@app.route("/", methods=['POST'])


#DELETE URLs
@app.route("/", methods=['DELETE'])
