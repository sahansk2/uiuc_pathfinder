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


#POST URLs (CREATE)
@app.route("/courses", methods=['POST'])
def x():
    return

@app.route("/professors", methods=['POST'])
def x():
    return

@app.route("/sections", methods=['POST'])
def x():
    return

@app.route("/interests", methods=['POST'])
def x():
    return


#GET URLs (READ/SEARCH)
@app.route("/courses", methods=['GET'])
def x():
    return

@app.route("/professors", methods=['GET'])
def x():
    return

@app.route("/sections", methods=['GET'])
def x():
    return

@app.route("/interests", methods=['GET'])
def x():
    return


#PUT URLs (UPDATE)
@app.route("/courses", methods=['PUT'])
def x():
    return

@app.route("/professors", methods=['PUT'])
def x():
    return

@app.route("/sections", methods=['PUT'])
def x():
    return

@app.route("/interests", methods=['PUT'])
def x():
    return


#DELETE URLs 
@app.route("/courses", methods=['DELETE'])
def x():
    return

@app.route("/professors", methods=['DELETE'])
def x():
    return

@app.route("/sections", methods=['DELETE'])
def x():
    return

@app.route("/interests", methods=['DELETE'])
def x():
    return


#for prereqs, rev, context only need course department and course data
#courseinfo: course join sections join teaching course join professors join restrictions

@app.route("/niceprofessors", methods=['GET'])
def nice_profs():

@app.route("/prereqs", methods=['GET'])

@app.route("/prereqs", methods=['GET'])

@app.route("/rev", methods=['GET'])

@app.route("/context", methods=['GET'])

@app.route("/cinfo", methods=['GET'])
