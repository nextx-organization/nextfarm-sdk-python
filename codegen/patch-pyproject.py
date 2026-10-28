"""Adds PyPI metadata (description, license, URLs, classifiers) to the generated pyproject.toml."""
import re
import sys

path, sha = sys.argv[1], sys.argv[2]
s = open(path, encoding="utf-8").read()
meta = '''description = "Official Python client for the NextFarm API"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "NextFarm", email = "support@nextfarm.vn"}]
keywords = ["nextfarm", "agriculture", "api", "sdk", "openapi", "iot", "gis", "traceability"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries",
    "Typing :: Typed",
]
'''
s = re.sub(r'^description = .*\n', "", s, flags=re.M)
s = re.sub(r'^authors = .*\n', "", s, flags=re.M)
s = re.sub(r'^readme = .*\n', "", s, flags=re.M)
s = re.sub(r'^license = .*\n', "", s, flags=re.M)
s = s.replace("[project]\n", "[project]\n" + meta, 1)
s += f'''
[project.urls]
Homepage = "https://developers.nextfarm.vn/docs/sdk"
Documentation = "https://developers.nextfarm.vn"
Source = "https://github.com/nextx-organization/nextfarm-sdk-python"
Changelog = "https://github.com/nextx-organization/nextfarm-sdk-python/blob/main/CHANGELOG.md"
Issues = "https://github.com/nextx-organization/nextfarm-sdk-python/issues"

[tool.nextfarm]
spec-sha256 = "{sha}"
'''
s = s.replace('requires = ["pdm-backend"]', 'requires = ["pdm-backend==2.4.5"]')
open(path, "w", encoding="utf-8").write(s)
