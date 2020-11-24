from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
def Login_page():
	return render_template('hello.html')

@app.route('/student/home')
def student_home_page():
        return 'Hello Napier'

@app.route('/student/work')
def student_work_page():
        return 'Hello Napier'

@app.route('/student/feedback')
def student_feedback_page():
        return 'Hello Napier'

@app.route('/student/load')
def student_load_page():
        return 'Hello Napier'

@app.route('/staff/home')
def staff_home_page():
        return 'Hello Napier'

@app.route('/staff/work')
def staff_work_page():
        return 'Hello Napier'

@app.route('/staff/marking')
def staff_marking_page():
        return 'Hello Napier'

@app.route('/staff/load')
def staff_load_page():
        return 'Hello Napier'
