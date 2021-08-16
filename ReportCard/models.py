from django.db import models

# Create your models here.

class Student(models.Model):
    Round = models.CharField(max_length=200,null=True)
    FirstName = models.CharField(max_length=200,null=True)
    LastName = models.CharField(max_length=200,null=True)
    CandidateName = models.CharField(max_length=200,null=True)
    RegistrationNumber = models.CharField(max_length=200,null=True)
    Grade = models.CharField(max_length=200,null=True)
    NameOfSchool = models.CharField(max_length=300,null=True)
    Gender = models.CharField(max_length=100,null=True)
    dateOfBirth = models.CharField(max_length=200,null=True)
    City = models.CharField(max_length=500,null=True)
    DateOfTest = models.CharField(max_length=200,null=True)
    QuestionNo = models.CharField(max_length=200,null=True)
    CandidateChoice = models.CharField(max_length=200,null=True)
    CorrectChoice = models.CharField(max_length=200,null=True)
    Outcome = models.CharField(max_length=200,null=True)
    ScoreIfCorrect = models.CharField(max_length=200,null=True)
    CandidateScore = models.CharField(max_length=200,null=True)
    FinalResult = models.CharField(max_length=300,null=True)

    