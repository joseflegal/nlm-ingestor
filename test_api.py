# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pytest",
#     "flask"
# ]
# ///
from pathlib import Path
import pytest
from flask.testing import FlaskClient
from nlm_ingestor.ingestion_daemon.__main__ import app


@pytest.fixture(scope="session")
def sut() -> FlaskClient:
    return app.test_client()


@pytest.fixture
def resources():
    return Path.cwd() / "resources"


def assert_parser(sut: FlaskClient, file_path: Path) -> None:
    result = sut.post("/api/parseDocument", files={"file": open(file_path, "rb")})
    assert result.status_code == 200


def test_parser_with_pdf(sut: FlaskClient, resources: Path) -> None:
    assert_parser(sut, resources / "sample.pdf")


def test_parser_with_docx(sut: FlaskClient, resources: Path) -> None:
    assert_parser(sut, resources / "sample1.docx")
