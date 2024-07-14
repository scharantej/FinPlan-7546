
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'

# Sample data objects
goals = [
    {'id': 1, 'name': 'Buy a new car', 'target_amount': 20000, 'current_amount': 12000},
    {'id': 2, 'name': 'Save for retirement', 'target_amount': 100000, 'current_amount': 25000},
    {'id': 3, 'name': 'Go on a vacation', 'target_amount': 5000, 'current_amount': 1500}
]

transactions = [
    {'id': 1, 'goal_id': 1, 'amount': 500, 'date': '2023-03-08'},
    {'id': 2, 'goal_id': 2, 'amount': 1000, 'date': '2023-04-15'},
    {'id': 3, 'goal_id': 3, 'amount': 200, 'date': '2023-05-01'}
]

@app.route('/')
def homepage():
    return render_template('index.html', goals=goals, transactions=transactions)

@app.route('/create_goal', methods=['POST'])
def create_goal():
    name = request.form['name']
    target_amount = request.form['target_amount']
    current_amount = request.form['current_amount']
    goal = {'id': len(goals)+1, 'name': name, 'target_amount': target_amount, 'current_amount': current_amount}
    goals.append(goal)
    return redirect(url_for('homepage'))

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    goal_id = request.form['goal_id']
    amount = request.form['amount']
    date = request.form['date']
    transaction = {'id': len(transactions)+1, 'goal_id': goal_id, 'amount': amount, 'date': date}
    transactions.append(transaction)
    return redirect(url_for('homepage'))

@app.route('/view_plan')
def view_plan():
    return render_template('plan.html', goals=goals, transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
