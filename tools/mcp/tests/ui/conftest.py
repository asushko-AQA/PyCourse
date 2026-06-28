"""Shared pytest fixtures for the Playwright UI suite."""

from pathlib import Path
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

import pytest

TEST_PORT = 3100
TEST_HOST = "127.0.0.1"
READY_URL = f"http://{TEST_HOST}:{TEST_PORT}/en"
BASE_URL = f"http://{TEST_HOST}:{TEST_PORT}"
READY_TIMEOUT_SECONDS = 120

IS_WINDOWS = sys.platform == "win32"


def _repo_root() -> str:
    return str(Path(__file__).resolve().parents[4])


def _wait_until_ready(url: str, timeout: float) -> None:
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                if response.status == 200:
                    return
        except (urllib.error.URLError, ConnectionError, OSError) as exc:
            last_error = exc
        time.sleep(1)
    raise RuntimeError(
        f"Server at {url} did not become ready within {timeout:.0f}s"
        + (f" (last error: {last_error})" if last_error else "")
    )


def _terminate_process_tree(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    if IS_WINDOWS:
        try:
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                check=False,
                capture_output=True,
            )
        except Exception:
            proc.kill()
    else:
        try:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()
        except Exception:
            proc.kill()


@pytest.fixture(scope="session")
def base_url():
    """Yield the base URL of the app under test."""
    env_url = os.environ.get("E2E_BASE_URL")
    if env_url:
        yield env_url.rstrip("/")
        return

    repo_root = _repo_root()
    subprocess.run(
        "npm --prefix frontend run build",
        cwd=repo_root,
        shell=True,
        check=True,
    )

    creationflags = subprocess.CREATE_NEW_PROCESS_GROUP if IS_WINDOWS else 0
    proc = subprocess.Popen(
        f"npm --prefix frontend run start -- -p {TEST_PORT}",
        cwd=repo_root,
        shell=True,
        creationflags=creationflags,
    )

    try:
        _wait_until_ready(READY_URL, READY_TIMEOUT_SECONDS)
        yield BASE_URL
    finally:
        _terminate_process_tree(proc)


@pytest.fixture(scope="session", autouse=True)
def _configure_test_id_attribute(playwright):
    """Match get_by_test_id to data-automation-id."""
    playwright.selectors.set_test_id_attribute("data-automation-id")
