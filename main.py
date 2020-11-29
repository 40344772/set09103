from flask import Flask, render_template
app = Flask(__name__)

@app.route('/login')
def Login_page():
	return render_template('loginPage.html'), 200

@app.route('/student/home')
def student_home_page():
        return render_template('studentMain.html'), 200

@app.route('/student/work')
def student_work_page():
        return render_template('work.html'), 200

@app.route('/student/feedback')
def student_feedback_page():
        return render_template('feedback.html'), 200

@app.route('/student/load')
def student_load_page():
        return render_template('load.html'), 200

@app.route('/student/submit')
def student_submit_page():
        return render_template('submit.html'), 200

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

@app.route('/staff/tasks')
def staff_tasks_page():
        return render_template('teacherMarking.html'), 200
