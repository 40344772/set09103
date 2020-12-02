from flask import Flask
from flask import Flask, render_template, flash, redirect, request, session, abort, url_for, g
import os
from datetime import date
import loginDetails as dbHandler
import uploadDisplay as dbUpload 

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'pdf'

@app.route('/')
def home_page():
	return render_template('loginPage.html')
 
@app.route('/login', methods=['POST', 'GET'])
def Login_page():
	if request.method=='POST':
		users = dbHandler.userValidation(request.form['username'], request.form['password'])
		if len(users) != 0:
			type = dbHandler.typeFind(request.form['username'], request.form['password'])
			verify = dbHandler.getStud()
			if (type == verify):
				return redirect(url_for('student_home_page'))
			else:
				return redirect(url_for('staff_home_page'))
		else:
			return redirect(url_for('home_page'))
	else:
		return redirect(url_for('home_page'))

@app.route('/account')
def account_page():
	return render_template('newAccountPage.html')

@app.route('/create', methods=['POST', 'GET'])
def create_page():
        if not request.form['username']:
                return redirect(url_for('account_page'))
        elif not request.form['password']:
                return redirect(url_for('account_page'))
        else:
                dbHandler.insertUser(request.form['username'], request.form['password'], request.form['account'])
                return redirect(url_for('home_page'))

@app.route('/student/home')
def student_home_page():
	return render_template('studentMain.html'), 200

@app.route('/student/work')
def student_work_page():
	data = dbUpload.display()
	return render_template('work.html', data=data)

@app.route('/student/feedback')
def student_feedback_page():
	return render_template('feedback.html'), 200

@app.route('/student/load')
def student_load_page():
	return render_template('load.html'), 200

@app.route('/student/submit')
def student_submit_page():
	return render_template('submit.html'), 200

@app.route('/student/working')
def student_working_page():
	return render_template('studentWork.html'), 200

@app.route('/staff/home')
def staff_home_page():
	return render_template('techerHome.html'), 200

@app.route('/staff/work')
def staff_work_page():
	return render_template('workTeacher.html'), 200

@app.route('/staff/marking')
def staff_marking_page():
	return render_template('submitTeacher.html'), 200

@app.route('/staff/load')
def staff_load_page():
	return render_template('loadTeacher.html'), 200

@app.route('/staff/upload')
def staff_upload_page():
	return render_template('upload.html'), 200

@app.route('/upload/file', methods=['POST'])
def upload_file():
	uploaded_file = request.files['fleToUpload']
	if uploaded_file.filename != ' ':
		uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
		dbUpload.insertUpload(uploaded_file.filename, date.today())
	return redirect(url_for('staff_upload_page'))

@app.route('/staff/working')
def staff_tasks_page():
	return render_template('teacherMarking.html'), 200

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)
