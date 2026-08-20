"""Minimal example for ScreenshotDiff."""

from screenshotdiff import screenshotdiff


def main():
 runner = screenshotdiff({"name": "ScreenshotDiff", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()