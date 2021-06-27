from setuptools import setup

setup(
    name="mutt scripts",
    version="0.0.1",
    description="Do stuff for mutt",
    packages=["lib"],
    py_modules=["ical_to_todoist", "dump_ical"],
    entry_points={
        "console_scripts": ["ical_to_todoist=ical_to_todoist:main",
                            "dump_ical=dump_ical:main"],
    },
)
