from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
todo_list = []

def is_valid_email(email):
    # Simple email validation regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/')
def index():
    return render_template("index.html", todos=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Data validation
    if not task or not email or not priority:
        return redirect('/')
    if not is_valid_email(email):
        return redirect('/')
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Append the new to-do item as a dictionary
    todo_list.append({
        'task': task,
        'email': email,
        'priority': priority
    })
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)