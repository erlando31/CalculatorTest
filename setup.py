from setuptools import find_packages, setup

setup(
    name="sample-python-projects",
    version="1.0.0",
    author="erlandohbs.com",
    author_email="erlandohbs@gmail.com",
    packages=find_packages(),
    test_suite="test", 
    setup_requires=[
        "pytest-runner",
    ],
    # entry_points={
    #     'console_scripts': [
    #         'test = app.logParser:parserLogs',  # Reference to main() in logParser.py inside app/
    #     ],
    # },
    extras_require={
        'dev': [
            "pytest",
            "pytest-timeout",  # Additional testing libraries can be added here
        ],
    },
)
