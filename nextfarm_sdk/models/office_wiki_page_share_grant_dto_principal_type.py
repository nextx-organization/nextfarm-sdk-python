from typing import Literal

OfficeWikiPageShareGrantDtoPrincipalType = Literal['Department', 'Group', 'Guest', 'User']

OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_PRINCIPAL_TYPE_VALUES: set[OfficeWikiPageShareGrantDtoPrincipalType] = { 'Department', 'Group', 'Guest', 'User',  }

def check_office_wiki_page_share_grant_dto_principal_type(value: str) -> OfficeWikiPageShareGrantDtoPrincipalType:
    if value in OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_PRINCIPAL_TYPE_VALUES!r}")
