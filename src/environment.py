import os


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class EnvironmentVariables(Singleton):
    def __init__(self):
        self.signing_secret = None
        self.slack_token = None

    def get_signing_secret(self):
        if self.signing_secret is None:
            self.signing_secret = os.getenv("SIGNING_SECRET", "test")

        return self.signing_secret

    def get_slack_token(self):
        if self.slack_token is None:
            self.slack_token = os.getenv("SLACK_TOKEN", "test")

            # xoxb - 4590916338816 - 4560647416198 - I5LU9iyAb2YNityt8bEAG9ek

        return self.slack_token


env = EnvironmentVariables()
