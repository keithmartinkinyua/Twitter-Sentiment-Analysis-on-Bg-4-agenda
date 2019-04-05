from flask import Flask, jsonify
from Scripts import sentiment as s

api = Flask(__name__)
@api.route("/")
def index():
	return jsonify({
		"data": "Success"
		})

@api.route("/tweet/<message>", methods=["GET", "PUT"])
def data(message):
	sent = s.sentiment(str(message))
	if sent[0] == "pos":
		return jsonify({
			"message" : message,
			"response": "The message is positive with a confidence of {}".format(sent[1] * 100)
			})
	elif sent[0] == "neg":
		return jsonify({
			"message" : message,
			"response": "The message is negative with a confidence of {}".format(sent[1] * 100)
			})


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')