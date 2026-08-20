"""Runs ScreenshotDiff in demo mode with sample data."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from screenshotdiff.cli import main

if __name__ == "__main__":
 sys.exit(main(["run", "--demo", "--verbose"]))