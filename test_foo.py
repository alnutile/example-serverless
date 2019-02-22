from foo import Foo
from unittest import TestCase
import unittest
from unittest.mock import patch
from unittest import mock


class TestFoo(TestCase):
    def test_bar(self):
        foo = Foo()
        results = foo.yo({"form_field": "bar"})
        self.assertEqual("bar", results)

