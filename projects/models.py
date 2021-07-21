from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # Null(false) --> for database will not allow and blank(false) --> django forms will not allow submission
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    featured_image = models.ImageField(null=True, blank=True)
    # auto_now_add --> takes a timestamp when the obj is created.
    # auto_now     --> takes a timestamp everytime the obj is updated.
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tags = models.ManyToManyField('Tag', blank=True)

    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except ValueError:
            img = ''
        return img

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value + " - " + str(self.project)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
