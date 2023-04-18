from flask import Flask, render_template, request, redirect, url_for
from database import add_goal, add_subgoal, add_achievement, get_goals, get_subgoals, get_achievements, update_goal, delete_goal, update_subgoal, delete_subgoal, update_achievement, delete_achievement

app = Flask(__name__)

@app.route('/')
def index():
    goals = get_goals()
    subgoals = get_subgoals()
    achievements = get_achievements()
    return render_template('index.html', goals=goals, subgoals=subgoals, achievements=achievements)


if __name__ == '__main__':
    app.run(debug=True)

# In app.py

@app.route('/add_main_goal', methods=['GET', 'POST'])
def add_main_goal():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        deadline = request.form['deadline']

        add_goal(title, description, category, deadline)
        return redirect(url_for('index'))

    return render_template('add_main_goal.html')

# Add subgoal
@app.route('/add_subgoal', methods=['GET', 'POST'])
def add_subgoal_route():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        main_goal_id = int(request.form['main_goal_id'])
        deadline = request.form['deadline']

        add_subgoal(title, description, main_goal_id, deadline)
        return redirect(url_for('index'))
    return render_template('add_subgoal.html')

# Add achievement
@app.route('/add_achievement', methods=['GET', 'POST'])
def add_achievement_route():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        add_achievement(title, description)
        return redirect(url_for('index'))
    return render_template('add_achievement.html')

# Update subgoal
@app.route('/update_subgoal/<int:subgoal_id>', methods=['GET', 'POST'])
def update_subgoal_route(subgoal_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        deadline = request.form['deadline']

        update_subgoal(subgoal_id, title, description, deadline)
        return redirect(url_for('index'))
    return render_template('update_subgoal.html')

# Delete subgoal
@app.route('/delete_subgoal/<int:subgoal_id>', methods=['POST'])
def delete_subgoal_route(subgoal_id):
    delete_subgoal(subgoal_id)
    return redirect(url_for('index'))

# Update achievement
@app.route('/update_achievement/<int:achievement_id>', methods=['GET', 'POST'])
def update_achievement_route(achievement_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        update_achievement(achievement_id, title, description)
        return redirect(url_for('index'))
    return render_template('update_achievement.html')

# Delete achievement
@app.route('/delete_achievement/<int:achievement_id>', methods=['POST'])
def delete_achievement_route(achievement_id):
    delete_achievement(achievement_id)
    return redirect(url_for('index'))

