import os
from pathlib import Path

from robocorp import browser
from robocorp.tasks import task

OUTPUT_DIR = Path(os.getenv("ROBOT_ARTIFACTS", "output"))
START_URL = "https://www.join.agileengine.com/open-positions/"


@task
def get_open_positions():
    browser.configure(
        browser_engine="chromium", 
        screenshot="only-on-failure", 
        headless=True 
    )
    try:
        page = browser.goto(START_URL)
        page.click("label:text('Engineering')")

        element = page.locator("css=div.awsm-job-listings:not(.awsm-jobs-loading)")
        element.wait_for()
        element.screenshot(path="output/jobs.png")
        page.screenshot(path="output/page.png")
    finally:
        # A place for teardown and cleanups. (Playwright handles browser closing)
        print("Automation finished!")
