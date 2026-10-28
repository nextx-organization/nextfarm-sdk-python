from typing import Literal

OfficeCreateWikiPageRequestKind = Literal['Doc', 'Sheet']

OFFICE_CREATE_WIKI_PAGE_REQUEST_KIND_VALUES: set[OfficeCreateWikiPageRequestKind] = { 'Doc', 'Sheet',  }

def check_office_create_wiki_page_request_kind(value: str) -> OfficeCreateWikiPageRequestKind:
    if value in OFFICE_CREATE_WIKI_PAGE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_CREATE_WIKI_PAGE_REQUEST_KIND_VALUES!r}")
