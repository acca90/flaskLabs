from flask import Flask, jsonify, abort
app = Flask(__name__)

# GET LIST
@app.route("/contato", methods=['GET'])
def get_contato_list():
    abort(403)
    # return response('GET', None, [1,2,3])

# GET INSTANCE
# @app.route("/contato/<int:pk>/", methods=['GET'])
# def get_contato(pk):
#    return response('GET', pk, None)

# CREATE INSTANCE
@app.route("/contato", methods=['POST'])
def post_contato():
    return response('POST', 1, None)

# UPDATE INSTANCE
@app.route("/contato/<int:pk>/", methods=['PUT'])
def put_contato(pk):
	return response('PUT', pk, None)

# MERGE INSTANCE
@app.route("/contato/<int:pk>/", methods=['PATCH'])
def patch_contato(pk):
    return response('PUT', pk, None)

# DELETE INSTANCE
@app.route("/contato/<int:pk>/", methods=['DELETE'])
def delete_contato(pk):
    return response('DELETE', None, None)


# RESPONSE DEFAULT
def response(method, data, list): 
	return jsonify({
		'method': method,
		'data': data,
		'lista': list
	})
