from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)

    class Meta:
        ordering = ["created"]


class Course(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.CharField(max_length=30)
    owner = models.ForeignKey(
        "auth.User",default=1, related_name="courses", on_delete=models.CASCADE
    )
    desc = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.title[:30]}..."
