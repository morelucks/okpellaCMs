# Create a new management command, e.g., hash_passwords.py
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from ..corpMembers.models import User  # Import your User model

class Command(BaseCommand):
    help = 'Migrate plaintext passwords to hashed passwords'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if user.password.startswith('!bcrypt'):
                # Skip already hashed passwords (for example, if you've already hashed some passwords)
                continue
            user.password = make_password(user.password)
            user.save()
        self.stdout.write(self.style.SUCCESS('Passwords have been hashed successfully.'))
