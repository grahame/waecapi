from setuptools import setup, find_packages

dev_requires = ['flake8', 'nose']
install_requires = ['requests>=2.2']

setup(
    author = "Grahame Bowland",
    author_email = "grahame@angrygoats.net",
    description = "WAEC API access",
    license = "GPL3",
    keywords = "openssh ssh",
    url = "https://github.com/grahame/waecapi",
    name = "waecapi",
    version = "0.0.1",
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    extras_require = {
        'dev': dev_requires
    },
    install_requires = install_requires,
    entry_points = {
        'console_scripts': [
            'waecapi = waecapi.cli:main',
        ],
    }
)
