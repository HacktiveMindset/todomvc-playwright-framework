import pytest, os, shutil, subprocess
from playwright.sync_api import sync_playwright
from datetime import datetime

@pytest.fixture(params=["chromium","firefox"])
def page(request):
    with sync_playwright() as p:
        browser=getattr(p,request.param).launch(headless=False)
        context=browser.new_context(viewport={"width":1280,"height":720})
        page=context.new_page()
        yield page
        context.close()
        browser.close()

def pytest_sessionfinish(session, exitstatus):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    results_dir = os.path.join("reports", "_allure_tmp")
    final_dir = os.path.join("reports", timestamp)

    os.makedirs(final_dir, exist_ok=True)

    # Important: use allure.bat explicitly (Windows fix)
    subprocess.run([
        "C:\\allure-2.36.0\\bin\\allure.bat",
        "generate",
        results_dir,
        "-o",
        final_dir,
        "--clean"
    ])

    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)