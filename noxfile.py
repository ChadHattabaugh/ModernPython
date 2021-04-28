import nox

@nox.session(python=["3.8.9", "3.9.4"])
def tests(session): 
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")