import tempfile

import nox
from nox.sessions import Session
import nox_poetry

nox.options.sessions = "lint", "mypy", "tests"
locations = "src", "tests", "noxfile.py"


@nox_poetry.session(python=["3.9"])
def tests(session: Session) -> None:
    args = session.posargs or ["--cov", "-m", "not e2e"]
    env = {
        "ORGANIZATION_CATALOG_BASE_URI": "https://organizations.fellesdatakatalog.digdir.no"
    }
    session.install(".", "coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", env=env, *args)


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
def mypy(session: Session) -> None:
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)
