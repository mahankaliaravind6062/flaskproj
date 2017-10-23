from app import db

class Question(db.Model):
	__tablename__ = 'question'
	id = db.Column(db.Integer, primary_key=True)
	desc = db.Column(db.Text, unique=True)

	def __repr__(self):
		return '<Question %r>' % (self.desc)
		
class Option(db.Model):
	__tablename__ = 'option'
	id = db.Column(db.Integer, primary_key=True)
	desc = db.Column(db.Text)
	question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

	def __repr__(self):
		return '<Option %r>' % (self.desc)		
		
class Report(db.Model):
	__tablename__ = 'report'
	id = db.Column(db.Integer, primary_key=True)
	option = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
	question = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
	ucount = db.Column(db.Integer)
	def __repr__(self):
		return '<Report %r %r %r>' % (self.question,self.option,self.ucount)	


		