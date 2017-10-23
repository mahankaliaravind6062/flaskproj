from flask import Flask,render_template,abort,jsonify


@app.route('/')
def home():
	return "Hello world"

@app.route('/todo/api/questions', methods=['GET'])
def get_questions():
	'''
	This is an api call to get the questions and options
	for the survey	
	'''
	
	if len(questions) == 0:
		abort(404)
		
	question = 	questions[0]
	question['options'] = [option for option in options if option['question'] == question['id']]
	if len(options) == 0:
		abort(404)
	return jsonify({'data': question})
	
	
def welcome():
	return render_template('survey.html')