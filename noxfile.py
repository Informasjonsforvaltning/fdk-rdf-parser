import tempfile

import nox
from nox.sessions import Session
import nox_poetry

nox.options.sessions = "lint", "mypy", "safety", "tests"
locations = "src", "tests", "noxfile.py"


@nox.session(python="3.8")
def tests(session: Session) -> None:
    args = session.posargs or ["--cov", "-m", "not e2e"]
    env = {
        "ORGANIZATION_CATALOGUE_BASE_URI": "https://organizations.fellestestkatalog.no"
    }
    nox_poetry.install(session, nox_poetry.WHEEL)
    nox_poetry.install(session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock")
    session.run("pytest", env=env, *args)


@nox.session(python="3.8")
def lint(session: Session) -> None:
    args = session.posargs or locations
    nox_poetry.install(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
        "pep8-naming",
    )
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session: Session) -> None:
    args = session.posargs or locations
    nox_poetry.install(session, "black")
    session.run("black", *args)


@nox.session(python="3.8")
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
        nox_poetry.install(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.8")
def coverage(session: Session) -> None:
    """Upload coverage data."""
    nox_poetry.install(session, "coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


@nox.session(python="3.8")
def mypy(session: Session) -> None:
    args = session.posargs or locations
    nox_poetry.install(session, "mypy")
    session.run("mypy", *args)
