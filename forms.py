from django import forms
from .models import Goal, Subtask, JournalEntry, Achievement, Note, Attachment


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'due_date', 'completed']

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['title', 'description', 'deadline', 'goal']  # Change due_date to deadline


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content', 'goal']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description', 'goal', 'date_achieved']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'goal']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file', 'goal']
