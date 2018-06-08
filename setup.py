from setuptools import find_packages, setup

with open("README.rst", "r") as f:
    readme = f.read()

with open("CHANGELOG", "r") as f:
    changelog = f.read()


if __name__ == "__main__":
    setup(
        name="flask-debugtoolbar-warnings",
        version="0.0.1.dev",
        author="Alec Nikolas Reiter",
        author_email="alecreiter@gmail.com",
        description="Adds warnings support to Flask-Debugtoolbar",
        long_description=readme + "\n\n" + changelog,
        license="MIT",
        packages=find_packages("src", exclude=["test"]),
        package_dir={"": "src"},
        package_data={"": ["LICENSE", "README.rst", "CHANGELOG"]},
        include_package_data=True,
        zip_safe=False,
        url="https://github.com/flaskbb/flask-debugtoolbar-warnings",
        keywords=["flask", "debug", "warnings"],
        project_links={
            "Code": "https://github.com/flaskbb/flask-debugtoolbar-warnings",
            "Issue Tracker": "https://github.com/flaskbb/flask-debugtoolbar-warnings",
        },
        python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
        classifiers=[
            "Development Status :: 1 - Planning",
            "Framework :: Flask",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
        ],
        install_requires=["Flask>=0.12.0", "flask-debugtoolbar>=0.10.0"],
    )
