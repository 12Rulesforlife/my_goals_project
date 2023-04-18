from flask import Flask, render_template, request, redirect, url_for
from database import get_goals, add_goal, update_goal, delete_goal, get_subgoals, add_subgoal, update_subgoal, delete_subgoal, get_achievements, add_achievement, update_achievement, delete_achievement

app = Flask(__name__)

@app.route('/')
def index():
    goals = get_goals()
    subgoals = get_subgoals()
    achievements = get_achievements()
    return render_template('index.html', goals=goals, subgoals=subgoals, achievements=achievements)

@app.route('/add_main_goal', methods=['GET', 'POST'])
def add_main_goal():
    ...

@app.route('/add_subgoal', methods=['GET', 'POST'])
def add_subgoal_route():
    ...

@app.route('/add_achievement', methods=['GET', 'POST'])
def add_achievement_route():
    ...

@app.route('/update_subgoal/<int:subgoal_id>', methods=['GET', 'POST'])
def update_subgoal_route(subgoal_id):
    ...

@app.route('/delete_subgoal/<int:subgoal_id>', methods=['POST'])
def delete_subgoal_route(subgoal_id):
    ...

@app.route('/update_achievement/<int:achievement_id>', methods=['GET', 'POST'])
def update_achievement_route(achievement_id):
    ...

@app.route('/delete_achievement/<int:achievement_id>', methods=['POST'])
def delete_achievement_route(achievement_id):
    ...

if __name__ == '__main__':
    app.run(debug=True)
