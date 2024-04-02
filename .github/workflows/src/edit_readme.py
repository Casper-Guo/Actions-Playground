import json
import os

if __name__ == "__main__":
    issue_content = json.loads(os.environ.get('ISSUE_CONTENT', '""'))
    print(issue_content)
