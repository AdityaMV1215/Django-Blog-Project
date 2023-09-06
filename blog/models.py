from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Email(models.Model):
    address = models.CharField(max_length=100)
    domain = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.address}@{self.domain}"


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} (+{self.code})"
    
    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5, validators=[MinLengthValidator(5), MaxLengthValidator(5)])
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.street}, {self.city} {self.postal_code}, {self.country}"
    
    class Meta:
        verbose_name_plural = "Addresses"
    
class Phone(models.Model):
    number = models.CharField(max_length=10, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    type = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.country} {self.number}"
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=500)
    date = models.DateField()
    image = models.ImageField(upload_to="posts", null=True)
    content = models.TextField(max_length=None)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name="comments")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    text = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f"Comment by {self.first_name} {self.last_name} rated as {self.rating}"




