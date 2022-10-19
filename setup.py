from setuptools import setup

setup(
    name="discbot",
    version="0.0.1",
    packages=["discbot"],
    package_dir={"": "src"},
    install_requires=["discord.py==2.0.1", "python-dotenv==0.21.0", "requests==2.28.1", "black==22.10.0"],
)
