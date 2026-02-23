from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        for team in Team.objects.all():
            team.members.clear()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', superpower='Powered Armor')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', superpower='Super Soldier')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', superpower='Detective')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', superpower='Flight')

        # Add members to teams
        marvel.members.add(ironman, captain)
        dc.members.add(batman, superman)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2026-02-23')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2026-02-23')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=200)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
