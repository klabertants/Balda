from balda.settings import BASE_DIR
from django.test import TestCase
from subprocess import call, Popen

import os
import sys
import pkg_resources
import time
import subprocess

class SystemTest(TestCase):

    def test_is_venv(self):
        self.assertNotEqual(sys.prefix, sys.base_prefix)

    def test_are_requirements_installed(self):
        with open(os.path.join(BASE_DIR, 'requirements.txt')) as req:
            deps = []
            for dep in req.readlines():
                deps.append(dep.strip())

        self.assertTrue(pkg_resources.require(deps))

    def test_migrations(self):
        for cmd in ["makemigrations", "migrate"]:
            for target in ["", "balda_game"]:
                return_code = call(
                    "python manage.py " + cmd + " " + target,
                    shell=True
                )
                self.assertEqual(return_code, 0)

    def test_server_launch(self):
        return_code = call(
            "python manage.py runserver",
            shell=True
        )
        self.assertEqual(return_code, 0)
