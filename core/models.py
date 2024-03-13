from typing import Iterable
from django.db import models


# Create your models here.
class BlogViews(models.Model):
    id = models.AutoField(primary_key=True)
    blogId = models.IntegerField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    ipAddress = models.CharField(max_length=255)
    userAgent = models.CharField(max_length=255)

    def __str__(self):
        return f"Blog {self.blogId} - {self.dateCreated} - {self.ipAddress} - {self.userAgent}"

    class Meta:
        db_table = "BlogViews"


class GameReviews(models.Model):
    id = models.AutoField(primary_key=True)
    gameName = models.CharField(max_length=255)
    imgLink = models.CharField(max_length=255)
    yearPublished = models.IntegerField()
    hoursPlayed = models.IntegerField()
    notes = models.TextField()
    gameplay = models.IntegerField()
    storytelling = models.IntegerField()
    characterDesign = models.IntegerField()
    graphics = models.IntegerField()
    soundDesign = models.IntegerField()
    suspense = models.IntegerField()
    difficulty = models.IntegerField()
    replayability = models.IntegerField()
    emotionalImpact = models.IntegerField()
    performance = models.IntegerField()
    overallRating = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        gameplay_score = int(self.gameplay * 6.5 * 10)
        storytelling_score = int(self.storytelling * 7.3 * 10)
        characterDesign_score = int(self.characterDesign * 23.6 * 10)
        graphics_score = int(self.graphics * 10.3 * 10)
        soundDesign_score = int(self.soundDesign * 9.4 * 10)
        suspense_score = int(self.suspense * 13.3 * 10)
        difficulty_score = int(self.difficulty * 6.5 * 10)
        replayability_score = int(self.replayability * 1.7 * 10)
        emotionalImpact_score = int(self.emotionalImpact * 4.5 * 10)
        performance_score = int(self.performance * 17.0 * 10)

        self.overallRating = int((
            gameplay_score
            + storytelling_score
            + characterDesign_score
            + graphics_score
            + soundDesign_score
            + suspense_score
            + difficulty_score
            + replayability_score
            + emotionalImpact_score
            + performance_score
        )/100)
        # Saving the overall rating
        super(GameReviews, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.gameName)

    class Meta:
        db_table = "GameReviews"
