import nox

python_versions = ["3.8.9", "3.9.4"]
locations = "src", "tests", "noxfile.py"

nox.options.sessions = "lint", "tests"


@nox.session(python=python_versions)
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e3e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=python_versions)
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-isort", "isort", "flake8-bugbear")
    session.run("flake8", *args)


@nox.session(python=python_versions)
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
