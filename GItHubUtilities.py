import sys
from github import Github


def create_repository(new_repository_name: str) -> bool:
    my_github = Github('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')
    user = my_github.get_user()
    new_repo = user.create_repo(new_repository_name)

    if new_repo:
        return True
    else:
        return False


if __name__ == '__main__':
    new_repo_name = sys.argv[0]

    if create_repository(new_repo_name):
        print('Ok')
    else:
        print('Error')
