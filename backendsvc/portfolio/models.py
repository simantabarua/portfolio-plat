from django.db import models
from users.models import User

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Templates(models.Model):
    pass

class UserProfesstion(BaseClass):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    template = models.OneToOneField(Templates, on_delete=models.CASCADE)

class SocialLink(BaseClass):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    other_link = models.JSONField(blank=True, null=True) # for additional links


class Education(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class Project(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tech_stack = models.JSONField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)


class Service(BaseClass):
    """
        For freelancers
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True, null=True)


class BlogPost(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.JSONField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    cover_image = models.URLField(blank=True, null=True)


class Certification(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certifications")
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)


class OpenSourceContribution(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="open_source_contributions")
    project = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    repository_url = models.URLField()