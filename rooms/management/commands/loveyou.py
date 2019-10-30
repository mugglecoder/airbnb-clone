from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "help me basecommand"

    def add_arguments(self, parser):
        parser.add_argument("--times", help="command help test")

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))

