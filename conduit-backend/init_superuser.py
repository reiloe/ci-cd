from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.environ["DJANGO_SU_NAME"]
email = os.environ["DJANGO_SU_EMAIL"]
password = os.environ["DJANGO_SU_PASSWORD"]

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created.")
else:
    print(f"Superuser '{username}' already exists.")