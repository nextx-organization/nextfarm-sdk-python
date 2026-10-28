from typing import Literal

OfficeRequestWikiAccessRequestLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_REQUEST_WIKI_ACCESS_REQUEST_LEVEL_VALUES: set[OfficeRequestWikiAccessRequestLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_request_wiki_access_request_level(value: str) -> OfficeRequestWikiAccessRequestLevel:
    if value in OFFICE_REQUEST_WIKI_ACCESS_REQUEST_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_REQUEST_WIKI_ACCESS_REQUEST_LEVEL_VALUES!r}")
