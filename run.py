import os
import json

with open('data/data/commits.json') as fd:
    commits = json.load(fd)

try:
    with open('data/data/runs.json') as fd:
        runs = json.load(fd)

except FileNotFoundError:
    runs = {}


for commit in commits:
    commit_id = commit['commit']

    if commit['commit'] in runs:
        continue

    print('Running', commit['message'])
    os.system(f'(cd repo && git checkout {commit_id})')

    os.system('python3 repo/src/compute.py')

    with open('out.json') as fd:
        runs[commit_id] = json.load(fd)

    print(runs[commit_id])

with open('data/data/runs.json', 'w') as fd:
    json.dump(runs, fd, indent=1)
