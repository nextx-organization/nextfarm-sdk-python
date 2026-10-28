from typing import Literal

OfficeShareWikiPageRequestLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_SHARE_WIKI_PAGE_REQUEST_LEVEL_VALUES: set[OfficeShareWikiPageRequestLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_share_wiki_page_request_level(value: str) -> OfficeShareWikiPageRequestLevel:
    if value in OFFICE_SHARE_WIKI_PAGE_REQUEST_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_SHARE_WIKI_PAGE_REQUEST_LEVEL_VALUES!r}")
