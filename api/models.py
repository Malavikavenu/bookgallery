from django.db import models


class Books(models.Model):
 
    title=models.CharField(max_length=200)

    author=models.CharField(max_length=200)

    language=models.CharField(max_length=200)

    price=models.FloatField()

    genre=models.CharField(max_length=200)

    @property
    def reviews(self):
        return Review.objects.filter(book_object=self)
    
    @property
    def review_count(self):

        return self.reviews.count()
    
    @property
    def avg_rating(self):

        reviews=self.reviews
        avg=0

        if reviews:

            avg=sum([r.rating for r in reviews])/self.review_count

        return avg




    def __str__(self):

        return self.title

from django.core.validators import MinValueValidator,MaxValueValidator
class Review(models.Model):

    book_object=models.ForeignKey(Books,on_delete=models.CASCADE)

    comment=models.CharField(max_length=200)

    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    user=models.CharField(max_length=200)

    

