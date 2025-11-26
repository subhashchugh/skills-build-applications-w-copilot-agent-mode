from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user=ironman.name, type='Running', duration=30)
        Activity.objects.create(user=captain.name, type='Cycling', duration=45)
        Activity.objects.create(user=batman.name, type='Swimming', duration=60)
        Activity.objects.create(user=superman.name, type='Yoga', duration=20)

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=75)
        Leaderboard.objects.create(team=dc.name, points=80)

        # Workouts
        Workout.objects.create(name='HIIT', difficulty='Hard')
        Workout.objects.create(name='Cardio', difficulty='Medium')
        Workout.objects.create(name='Stretching', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
