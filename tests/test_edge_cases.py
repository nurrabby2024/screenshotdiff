import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_empty_input_is_handled():
 from screenshotdiff.validators import is_required
 import pytest
 with pytest.raises(ValueError):
 is_required("", "name")


def test_bounds_are_enforced():
 from screenshotdiff.validators import is_range
 import pytest
 with pytest.raises(ValueError):
 is_range(9999, 0, 10, "count")


def test_slug_validation():
 from screenshotdiff.validators import is_slug
 assert is_slug("hello-world") == "hello-world"