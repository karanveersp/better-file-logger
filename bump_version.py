import sys
import re

new_version = sys.argv[1]

with open("simple_file_logger\__init__.py", "rt") as t:
    text = t.read()

updated_text = re.sub(r"'(\d+\.\d+\.\d+)'", f"'{new_version}'", text)
with open("simple_file_logger\__init__.py", "wt") as t:
    t.write(updated_text)


with open("pyproject.toml", "rt") as f:
    text = f.read()

updated_text = re.sub(
    r"version = \"\d+\.\d+\.\d+\"", f'version = "{new_version}"', text
)

with open("pyproject.toml", "wt") as f:
    f.write(updated_text)
