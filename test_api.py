# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pytest",
#     "flask",
#     "httpx>=0.28.1",
# ]
# ///
import httpx
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def sut() -> httpx.Client:
    return httpx.Client(base_url="http://localhost:5010")


@pytest.fixture
def resources():
    return Path.cwd() / "resources"


def assert_parser(sut: httpx.Client, file_path: Path) -> None:
    result = sut.post("/api/parseDocument", files={"file": open(file_path, "rb")})
    assert result.status_code == 200


def test_parser_with_pdf(sut: httpx.Client, resources: Path) -> None:
    assert_parser(sut, resources / "sample.pdf")


def test_parser_with_docx(sut: httpx.Client, resources: Path) -> None:
    assert_parser(sut, resources / "sample1.docx")
