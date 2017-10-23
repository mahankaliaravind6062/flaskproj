from flask import Flask,render_template,abort,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from models import Question,Option

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(Option, db.session))

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
	
	
if __name__ == '__main__':
	app.run(debug=True)