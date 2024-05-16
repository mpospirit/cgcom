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


class ToiletReview(models.Model):
    id = models.AutoField(primary_key=True)
    toiletName = models.CharField(max_length=255)
    imgLink = models.CharField(max_length=255)
    notes = models.TextField()
    cleanliness = models.IntegerField()
    toiletPaper = models.IntegerField()
    smell = models.IntegerField()
    bidetNozzle = models.IntegerField()
    soap = models.IntegerField()
    comfort = models.IntegerField()
    lighting = models.IntegerField()
    airiness = models.IntegerField()
    doorLock = models.IntegerField()
    flush = models.IntegerField()
    overallRating = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        cleanliness_score = int(self.cleanliness * 10.0 * 10)
        toiletPaper_score = int(self.toiletPaper * 14.0 * 10)
        smell_score = int(self.smell * 3.0 * 10)
        bidetNozzle_score = int(self.bidetNozzle * 13.0 * 10)
        soap_score = int(self.soap * 6.0 * 10)
        comfort_score = int(self.comfort * 2.0 * 10)
        lighting_score = int(self.lighting * 3.0 * 10)
        airiness_score = int(self.airiness * 3.0 * 10)
        doorLock_score = int(self.doorLock * 27.0 * 10)
        flush_score = int(self.flush * 18.0 * 10)

        self.overallRating = int((
            cleanliness_score
            + toiletPaper_score
            + smell_score
            + bidetNozzle_score
            + soap_score
            + comfort_score
            + lighting_score
            + airiness_score
            + doorLock_score
            + flush_score
        )/100)
        # Saving the overall rating
        super(ToiletReview, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.toiletName)
    
    class Meta:
        db_table = "ToiletReview"


class AlbumReview(models.Model):
    id = models.AutoField(primary_key=True)
    albumName = models.CharField(max_length=255)
    artistName = models.CharField(max_length=255)
    imgLink = models.CharField(max_length=255)
    yearReleased = models.IntegerField()
    overallRating = models.IntegerField()

    def __str__(self):
        return f"{self.albumName} - {self.artistName}"
    
    class Meta:
        db_table = "AlbumReview"


class BookReview(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=255)
    authorName = models.CharField(max_length=255)
    imgLink = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    overallRating = models.IntegerField()

    def __str__(self):
        return f"{self.bookName} - {self.authorName}"
    
    class Meta:
        db_table = "BookReview"