from setuptools import setup

setup(
    # The name of our pip package
    name='pytouch',
    # The Python packages in this project
    packages=[
        # This is the `pytouch` folder that contains __init__.py and pytouch.py
        'pytouch',
    ],
    install_requires=[
        # These are pip dependencies we'll require
        'mock',
    ],
    version="0.0.1",
    entry_points={
        'console_scripts': [
            # We use this line to map our `main()` method in pytouch.py
            # to a shell command `pytouch`
            'pytouch = pytouch.pytouch:main',
        ],
    },
)
