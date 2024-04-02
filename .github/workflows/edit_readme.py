import json
import os

if __name__ == "__main__":
    issue_content = json.loads(os.environ.get('ISSUE_CONTENT', '""'))
    print([f for f in os.listdir(".") if os.path.isfile(f)])
    print(issue_content)
