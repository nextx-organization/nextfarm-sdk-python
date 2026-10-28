from typing import Literal

OfficeShareWikiPageRequestPrincipalType = Literal['Department', 'Group', 'Guest', 'User']

OFFICE_SHARE_WIKI_PAGE_REQUEST_PRINCIPAL_TYPE_VALUES: set[OfficeShareWikiPageRequestPrincipalType] = { 'Department', 'Group', 'Guest', 'User',  }

def check_office_share_wiki_page_request_principal_type(value: str) -> OfficeShareWikiPageRequestPrincipalType:
    if value in OFFICE_SHARE_WIKI_PAGE_REQUEST_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_SHARE_WIKI_PAGE_REQUEST_PRINCIPAL_TYPE_VALUES!r}")
