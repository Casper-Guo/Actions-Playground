import json
import re
import os


def parse_response(response: str) -> tuple[str]:
    """Separate the individual responses in the full response body."""
    # filter out potential empty string in the first split
    fields = [field for field in response.split("###") if field]

    # fetch the responses in each field
    # see README for assumptions about JSON formatting
    return tuple(re.search(r"\n+\s*(.*)\s*$", field.rstrip()).group(1)
                 for field in fields)


def shorten_url(url: str) -> str:
    "Remove query strings from submitted URLs."
    # Capture the url starting at www until the first question mark
    return re.search(r"^(http[s]?:\/\/)?([^\s\?]*)\?*", url).group(2)


def format_addition(response: tuple[str]) -> str:
    """Format issue response to a line in README.

    Change if README format and form questions drifts from assumptions listed in README
    and update README accordingly.
    """
    company, career_url, pos, pos_url, location, degree, note = response
    career_url = shorten_url(career_url)
    pos_url = shorten_url(pos_url)
    return f"| [{company}]({career_url}) | [{pos}]({pos_url}) | {location} | {degree} | {note if note != '_No response_' else ''}".strip()


if __name__ == "__main__":
    form_body = json.loads(os.environ.get('ISSUE_CONTENT', '""'))["body"]
    # with open(".github/workflows/test.json", "r") as f:
    #     form_body = json.load(f)["body"]
    response = parse_response(form_body)

    with open("README.md", "a") as readme:
        readme.write("\n")
        readme.write(format_addition(response))
