import nox

python_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]


@nox.session
def tests(session):
    """Run the test suite."""
    session.install(".[test]")
    session.env["PYTHONPATH"] = "src"
    session.run("pytest")


@nox.session
def docs(session):
    """Build the documentation."""
    session.install(".[docs]")
    session.run("sphinx-build", "docs", "docs/_build")
    session.run("python", "-m", "webbrowser", "docs/_build/index.html")


@nox.session
def format(session):
    """Format the codebase using ruff-format."""
    session.install("ruff", "ruff-format")
    session.run("ruff", "check", "--fix", ".")
    session.run("ruff-format", ".")
