from setuptools import setup

setup(
    name="venaribot",
    version="0.0.1",
    packages=["venaribot"],
    package_dir={"": "src"},
    install_requires=[
        "discord-py-interactions==4.3.4",
        "tweepy==4.10.1",
        "python-dotenv==0.21.0",
        "psycopg2-binary==2.9.3",
        "pytest==7.1.3",
        "beautifulsoup4==4.11.1",
        "asyncpg==0.26.0",
        "SQLAlchemy==2.0.0b2",
        "aiohttp==3.8.1",
        "async_lru==1.0.3",
        "oauthlib==3.2.0",
        "nest-asyncio==1.5.5",
        "interactions-files==1.1.5",
    ],
)
