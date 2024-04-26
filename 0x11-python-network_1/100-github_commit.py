from sys import argv
import requests

"""
gets 10 commits
"""


if __name__ == "__main__":
    """
    argv[1] = repo
    argv[2] = owner
    """
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1])).json()
    count = 0
    for commit in response:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, name))
        count += 1
        if count == 10:
            break
