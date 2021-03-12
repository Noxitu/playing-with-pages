import os
import json

VALID_CHARS = '0123456789abcdef'

os.system('(cd repo && git log main --oneline --reverse) | grep -E "^\w+ Merge pull request #" > list.txt')

commits = []

with open('list.txt') as fd:
    for line in fd:
        commit_id, message = line.split(' ', 1)

        if any(c not in VALID_CHARS for c in commit_id):
            raise Exception('')

        commits.append({
            'commit': commit_id,
            'message': message
        })

os.makedirs('data/data', exist_ok=True)

with open('data/data/commits.json', 'w') as fd:
    json.dump(commits, fd, indent=1)
