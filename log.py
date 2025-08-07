from git import Repo
from datetime import datetime

repo_path = './../TVshowapp'

repo = Repo(repo_path)
assert not repo.bare

last_commits = list(repo.iter_commits("main", max_count=5))

for commit in last_commits: 
    print("Commit: ", commit.hexsha)
    print("Committer: ", commit.author)
    print("Message: ", commit.message)
    print("Date: ", commit.committed_date)

for item in repo.index.diff(None):
    print(item.a_path)


#
# repo.index.diff(None)
#does only list files that have not been staged

#repo.index.diff('Head')
#does only list files that have been staged
# #