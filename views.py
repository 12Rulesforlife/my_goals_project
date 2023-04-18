from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Goal, Subtask, JournalEntry, Achievement, Note, Attachment
from .forms import GoalForm, SubtaskForm, JournalEntryForm, AchievementForm, NoteForm, AttachmentForm

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    goals = Goal.objects.filter(user=request.user)
    subgoals_list = Subtask.objects.filter(goal__user=request.user)
    context = {'goals': goals, 'subgoals': subgoals_list}
    return render(request, 'index.html', context)

def new_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('set_a_goal:index')
    else:
        form = GoalForm()
    return render(request, 'add_main_goal.html', {'form': form})

def edit_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('set_a_goal:index')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'edit_goal.html', {'form': form})

def update_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save()
            return redirect('set_a_goal:index')
        else:
            print("Form is not valid. Errors: ", form.errors)
    else:
        form = GoalForm(instance=goal)
    return render(request, 'update_goal.html', {'form': form, 'goal': goal})

def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id, user=request.user)
    goal.delete()
    return redirect('set_a_goal:index')



def new_subtask(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id, user=request.user)
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.goal = goal
            subtask.save()
            return redirect('set_a_goal:index')
    else:
        form = SubtaskForm()
    return render(request, 'set_a_goal/new_subtask.html', {'form': form, 'goal': goal})




def edit_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, pk=subtask_id, goal__user=request.user)
    if request.method == 'POST':
        form = SubtaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save()
            return redirect('set_a_goal:index')
    else:
        form = SubtaskForm(instance=subtask)
    return render(request, 'set_a_goal/edit_subtask.html', {'form': form})


def delete_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, pk=subtask_id, goal__user=request.user)
    subtask.delete()
    return redirect('set_a_goal:index')


def update_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, pk=subtask_id, goal__user=request.user)
    if request.method == 'POST':
        form = SubtaskForm(request.POST, instance=subtask)
        if form.is_valid():
            subtask = form.save()
            return redirect('set_a_goal:index')
        else:
            print("Form is not valid. Errors: ", form.errors)
    else:
        form = SubtaskForm(instance=subtask)
    return render(request, 'set_a_goal/update_subtask.html', {'form': form, 'subtask': subtask})

def goals_overview(request, category=None, status=None):
    goals = Goal.objects.filter(user=request.user)

    if category:
        goals = goals.filter(category=category)

    if status:
        if status == 'completed':
            goals = goals.filter(subtask__completed_on__isnull=False)
        elif status == 'incomplete':
            goals = goals.filter(subtask__completed_on__isnull=True)

    context = {'goals': goals}
    return render(request, 'goals_overview.html', context)

def toggle_subtask(request, subtask_id):
    subtask = get_object_or_404(Subtask, pk=subtask_id, goal__user=request.user)
    subtask.completed = not subtask.completed
    subtask.save()
    return redirect('set_a_goal:index')

def journal(request):
    journal_entries = JournalEntry.objects.filter(user=request.user).order_by('-date')
    context = {'journal_entries': journal_entries}
    return render(request, 'set_a_goal/journal.html', context)

def new_journal_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.user = request.user
            journal_entry.save()
            return redirect('journal')
    else:
        form = JournalEntryForm()
    return render(request, 'set_a_goal/new_journal_entry.html', {'form': form})



def new_achievement(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.user = request.user
            achievement.goal = goal
            achievement.save()
            return redirect('goal_detail', goal_id=goal.id)
    else:
        form = AchievementForm()
    return render(request, 'set_a_goal/new_achievement.html', {'form': form, 'goal': goal})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_where_categories_are_displayed')
    else:
        form = CategoryForm()
    return render(request, 'set_a_goal/create_category.html', {'form': form})

def create_achievement(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.goal = goal
            achievement.save()
            return redirect('some_view_where_achievements_are_displayed')
    else:
        form = AchievementForm()
    return render(request, 'set_a_goal/create_achievement.html', {'form': form, 'goal': goal})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_where_notes_are_displayed')
    else:
        form = NoteForm()
    return render(request, 'set_a_goal/create_note.html', {'form': form})

def create_attachment(request):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view_where_attachments_are_displayed')
    else:
        form = AttachmentForm()
    return render(request, 'set_a_goal/create_attachment.html', {'form': form})

def new_note(request, journal_entry_id):
    # Your implementation here
    pass

def new_attachment(request, journal_entry_id):
    journal_entry = get_object_or_404(JournalEntry, id=journal_entry_id, user=request.user)
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.journal_entry = journal_entry
            attachment.save()
            return redirect('some_view_where_attachments_are_displayed')
    else:
        form = AttachmentForm()
    return render(request, 'set_a_goal/new_attachment.html', {'form': form, 'journal_entry': journal_entry})

@login_required
def view_achievement(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id, user=request.user)
    achievements = Achievement.objects.filter(goal=goal)
    context = {'goal': goal, 'achievements': achievements}
    return render(request, 'set_a_goal/view_achievement.html', context)

def new_note(request, journal_entry_id):
    journal_entry = get_object_or_404(JournalEntry, id=journal_entry_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.journal_entry = journal_entry
            note.save()
            return redirect('set_a_goal:journal')
    else:
        form = NoteForm()
    return render(request, 'set_a_goal/new_note.html', {'form': form, 'journal_entry': journal_entry})
