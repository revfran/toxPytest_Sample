# content of test_unittest_cleandir.py
import pytest
import unittest
from src.myFirstPackage.sample import Sample


class MyTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir() # change to pytest-provided temporary directory
        tmpdir.join("samplefile.ini").write("# foo")

    def test_method(self):
        with open("samplefile.ini") as f:
            s = f.read()
        assert "foo" in s

    # Test passing
    def test_sample_func(self):
        sample = Sample()
        assertValue = sample.func(2) == 3
        print('Testing assert: ', assertValue)
        assert assertValue

    # Test failing on purpose
    @pytest.mark.xfail(raises=AssertionError, reason='This test is a sample of expected failure')
    def test_false(self):
        assert False