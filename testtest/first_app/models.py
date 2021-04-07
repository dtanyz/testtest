from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
    )


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score to pass")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}--{self.topic}"


class Question(models.Model):
    question_text = models.CharField(max_length=260)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    number_of_lines = models.IntegerField()


class BFUser(models.Model):
    callsign = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # List all Go/NoGo items here
    bfa_pass = models.BooleanField(default=False)
    bfb_pass = models.BooleanField(default=False)
    opslimit_pass = models.BooleanField(default=False)
    sam_signed = models.BooleanField(default=False)
    opsbrief_signed = models.BooleanField(default=False)

    def update_score(self):
        boldface_a = AllABoldface.objects.get(bf_user=self.id)
        if boldface_a.is_complete:
            self.bfa_pass = True
        else:
            self.bfa_pass = False
        self.save()

    def __str__(self):
        return f"{self.callsign}"


class AllABoldface(models.Model):
    bf0 = models.CharField(max_length=25, blank=True)
    bf1 = models.CharField(max_length=25, blank=True)
    bf2 = models.CharField(max_length=25, blank=True)
    bf3 = models.CharField(max_length=25, blank=True)
    bf4 = models.CharField(max_length=25, blank=True)
    bf5 = models.CharField(max_length=25, blank=True)
    bf6 = models.CharField(max_length=25, blank=True)
    bf7 = models.CharField(max_length=25, blank=True)
    bf8 = models.CharField(max_length=25, blank=True)
    bf9 = models.CharField(max_length=25, blank=True)
    bf10 = models.CharField(max_length=25, blank=True)
    bf11 = models.CharField(max_length=25, blank=True)
    bf12 = models.CharField(max_length=25, blank=True)
    bf13 = models.CharField(max_length=25, blank=True)
    bf14 = models.CharField(max_length=25, blank=True)
    bf15 = models.CharField(max_length=25, blank=True)
    bf16 = models.CharField(max_length=25, blank=True)
    bf17 = models.CharField(max_length=25, blank=True)
    bf18 = models.CharField(max_length=25, blank=True)
    bf19 = models.CharField(max_length=25, blank=True)
    bf20 = models.CharField(max_length=25, blank=True)
    bf21 = models.CharField(max_length=25, blank=True)
    bf22 = models.CharField(max_length=25, blank=True)
    bf23 = models.CharField(max_length=25, blank=True)
    bf24 = models.CharField(max_length=25, blank=True)
    bf25 = models.CharField(max_length=25, blank=True)
    bf26 = models.CharField(max_length=25, blank=True)
    bf27 = models.CharField(max_length=25, blank=True)
    bf28 = models.CharField(max_length=25, blank=True)
    bf29 = models.CharField(max_length=25, blank=True)
    bf30 = models.CharField(max_length=25, blank=True)
    bf31 = models.CharField(max_length=25, blank=True)
    bf32 = models.CharField(max_length=25, blank=True)
    bf33 = models.CharField(max_length=25, blank=True)
    bf34 = models.CharField(max_length=25, blank=True)
    bf35 = models.CharField(max_length=25, blank=True)
    bf36 = models.CharField(max_length=25, blank=True)
    bf37 = models.CharField(max_length=25, blank=True)
    bf38 = models.CharField(max_length=25, blank=True)
    bf39 = models.CharField(max_length=25, blank=True)
    bf40 = models.CharField(max_length=25, blank=True)
    bf41 = models.CharField(max_length=25, blank=True)
    bf42 = models.CharField(max_length=25, blank=True)
    bf43 = models.CharField(max_length=25, blank=True)
    bf44 = models.CharField(max_length=25, blank=True)
    bf45 = models.CharField(max_length=25, blank=True)
    bf46 = models.CharField(max_length=25, blank=True)
    bf47 = models.CharField(max_length=25, blank=True)
    bf48 = models.CharField(max_length=25, blank=True)
    bf49 = models.CharField(max_length=25, blank=True)
    bf50 = models.CharField(max_length=25, blank=True)
    bf51 = models.CharField(max_length=25, blank=True)
    bf52 = models.CharField(max_length=25, blank=True)
    bf53 = models.CharField(max_length=25, blank=True)
    bf54 = models.CharField(max_length=25, blank=True)
    bf55 = models.CharField(max_length=25, blank=True)
    bf56 = models.CharField(max_length=25, blank=True)
    bf57 = models.CharField(max_length=25, blank=True)
    bf58 = models.CharField(max_length=25, blank=True)
    bf59 = models.CharField(max_length=25, blank=True)
    bf60 = models.CharField(max_length=25, blank=True)
    bf61 = models.CharField(max_length=25, blank=True)
    bf62 = models.CharField(max_length=25, blank=True)
    bf63 = models.CharField(max_length=25, blank=True)
    bf64 = models.CharField(max_length=25, blank=True)
    bf65 = models.CharField(max_length=25, blank=True)
    bf66 = models.CharField(max_length=25, blank=True)
    bf67 = models.CharField(max_length=25, blank=True)
    bf68 = models.CharField(max_length=25, blank=True)
    bf69 = models.CharField(max_length=25, blank=True)
    bf70 = models.CharField(max_length=25, blank=True)
    bf71 = models.CharField(max_length=25, blank=True)
    bf72 = models.CharField(max_length=25, blank=True)
    bf73 = models.CharField(max_length=25, blank=True)
    bf74 = models.CharField(max_length=25, blank=True)
    bf75 = models.CharField(max_length=25, blank=True)
    bf76 = models.CharField(max_length=25, blank=True)
    bf77 = models.CharField(max_length=25, blank=True)
    bf78 = models.CharField(max_length=25, blank=True)
    bf79 = models.CharField(max_length=25, blank=True)
    bf80 = models.CharField(max_length=25, blank=True)
    bf81 = models.CharField(max_length=25, blank=True)
    bf82 = models.CharField(max_length=25, blank=True)
    bf83 = models.CharField(max_length=25, blank=True)
    bf84 = models.CharField(max_length=25, blank=True)
    bf85 = models.CharField(max_length=25, blank=True)
    bf86 = models.CharField(max_length=25, blank=True)
    bf87 = models.CharField(max_length=25, blank=True)
    bf88 = models.CharField(max_length=25, blank=True)
    bf89 = models.CharField(max_length=25, blank=True)
    bf90 = models.CharField(max_length=25, blank=True)
    bf91 = models.CharField(max_length=25, blank=True)
    bf92 = models.CharField(max_length=25, blank=True)
    bf93 = models.CharField(max_length=25, blank=True)
    bf94 = models.CharField(max_length=25, blank=True)
    bf95 = models.CharField(max_length=25, blank=True)

    is_complete = models.BooleanField(default=False)

    bf_user = models.ForeignKey(BFUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.bf_user}"

    class Meta:
        verbose_name = "Boldface A Record"




# Ops Brief / EODD minutes models


class OpsBriefMinutes(models.Model):
    class TypeOfMinutes(models.TextChoices):
        ops_brief = "Ops Brief"
        eodd = "EODD"

    type_of_minutes = models.CharField(max_length=10, choices=TypeOfMinutes.choices, default=TypeOfMinutes.ops_brief)
    date = models.DateField()
    minutes_taker = models.CharField(max_length=20)
    duty_instructor = models.CharField(max_length=20)
    vetted = models.BooleanField(default=False)

    def __str__(self):
        return f"Minutes for {self.date} {self.type_of_minutes}"


class Minutes(models.Model):
    minutes_for = models.ForeignKey(OpsBriefMinutes, on_delete=models.CASCADE)
    who_talked = models.CharField(max_length=20)
    write_up = models.TextField()


class Absentee(models.Model):
    minutes = models.ForeignKey(OpsBriefMinutes, on_delete=models.CASCADE)
    absent_user = models.ForeignKey(BFUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.absent_user} have not signed {self.minutes}"