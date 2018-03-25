# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from pocket_monitor.mo import samples


class Command(BaseCommand):
    help = 'Sync projects, contracts and samples into DB'

    def __init__(self):
        self.samples_sync = samples.Sync()

    def handle(self, *args, **options):
        self.samples_sync.sync()
