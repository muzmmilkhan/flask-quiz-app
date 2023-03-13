from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# define a list of questions with their respective answers
questions = [
    {'id': 1, 'text': 'What is the capital of France?', 'answer': 'Paris'},
    {'id': 2, 'text': 'What is the largest country in the world?', 'answer': 'Russia'},
    {'id': 3, 'text': 'What is the currency of Japan?', 'answer': 'Yen'}
]

# define a dictionary to keep track of the user's answers
user_answers = {}

# define a route to display the quiz questions
@app.route('/')
def quiz():
    return render_template('quiz.html', questions=questions)

# define a route to handle the quiz submissions
@app.route('/submit', methods=['POST'])
def submit():
    # iterate through the questions and add the user's answers to the dictionary
    for question in questions:
        user_answers[question['id']] = request.form.get(str(question['id']))
    return redirect(url_for('results'))

# define a route to display the quiz results
@app.route('/results')
def results():
    # iterate through the questions and check the user's answers
    for question in questions:
        if user_answers[question['id']] == question['answer']:
            question['result'] = 'correct'
        else:
            question['result'] = 'incorrect'
    return render_template('results.html', questions=questions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
