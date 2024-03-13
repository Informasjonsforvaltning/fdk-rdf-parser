import tempfile

import nox
from nox.sessions import Session
import nox_poetry

nox.options.sessions = "lint", "mypy", "tests"
locations = "src", "tests", "noxfile.py"

python_versions = ["3.8", "3.9", "3.10", "3.11", "3.12"]


@nox_poetry.session(python=python_versions)
def tests(session: Session) -> None:
    args = session.posargs or ["--cov", "-m", "not e2e"]
    env = {
        "ORGANIZATION_CATALOG_BASE_URI": "https://organizations.fellesdatakatalog.digdir.no"
    }
    session.install(".", "coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", *args, env=env)


@nox_poetry.session(python=["3.9"])
def cache(session: Session) -> None:
    """Clear cache."""
    session.run(
        "bash",
        "-c",
        "for f in $(find . -maxdepth 1 -name '*cache*'); do rm -rf $f; done",
        external=True,
    )
    session.run(
        "bash",
        "-c",
        "for f in $(find . -maxdepth 4 -name '__pycache__'); do rm -rf $f; done",
        external=True,
    )


@nox_poetry.session(python=["3.9"])
def lint(session: Session) -> None:
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
        "pep8-naming",
    )
    session.run("flake8", *args)


@nox_poetry.session(python=["3.9"])
def black(session: Session) -> None:
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox_poetry.session(python=["3.9"])
def isort(session: Session) -> None:
    session.install("isort")
    session.run("isort", ".")


@nox_poetry.session(python=["3.9"])
def fixlint(session: Session) -> None:
    session.notify("isort")
    session.notify("black")


@nox_poetry.session(python=["3.9"])
def safety(session: Session) -> None:
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run(
            "safety", "check", f"--file={requirements.name}", "--output", "text"
        )


@nox_poetry.session(python=["3.9"])
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


@nox_poetry.session(python=["3.9"])
def tests3_9(session: Session) -> None:
    """Used for generating coverage files for codecov"""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    env = {
        "ORGANIZATION_CATALOG_BASE_URI": "https://organizations.fellesdatakatalog.digdir.no"
    }
    session.install(".", "coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", *args, env=env)


@nox_poetry.session(python=python_versions)
def mypy(session: Session) -> None:
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)
