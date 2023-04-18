from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Goal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    def __str__(self):
        return self.title

class Subtask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='subtasks')
    completed_on = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class JournalEntry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='journal_entries')

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='achievements')
    date_achieved = models.DateField()

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='notes')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='attachments')

    def __str__(self):
        return self.file.name

class MotivationalQuote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.content} - {self.author}"

class DailyProcess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_processes')
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
