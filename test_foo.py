from foo import Foo
from unittest import TestCase
import unittest
from unittest.mock import patch
from unittest import mock
import json


class TestFoo(TestCase):
    def test_bar(self):
        with open("tests/fixtures/request.json.json") as payload:
            payload = json.load(payload)
        foo = Foo()
        results = foo.yo({"form_field": "bar"})
        self.assertEqual("bar", results)

