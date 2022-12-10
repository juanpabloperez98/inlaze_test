from django.db import models
from users.models import User

# MODEL PUBLISHED
class Published(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='published_to_user'
    )
    title = models.CharField(max_length=70)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Published"
        verbose_name_plural = "Publishedes"
    

    def __str__(self):
        return f"{self.pk} {self.title}"