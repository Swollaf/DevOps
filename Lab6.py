from github import Github
import yaml

# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
data = yaml.safe_load(open('username-credentials.yml'))

# Extract the user and token from the data object
# 0. Complete these 2 lines below
user = data['creds']['username']
token = data['creds']['token']

# using an access token
g = Github(token)
repo = g.get_repo(user)

# Complete your tasks from here

# 1. Get all branches you have created for your public repo
branches = list(repo.get_branches())
print(branches)

# 2. Get all pull requests you have created
pulls = repo.get_pulls(state='close', sort='created', base='main')

for pr in pulls:
    print(pr)

# 3. Get a list of commits you have created in your `main` branch
commit = repo.get_commits("main")
print(list(commit))

