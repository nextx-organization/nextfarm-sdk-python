from typing import Literal

OfficeWikiPageShareGrantDtoGrantKind = Literal['DirectInvite', 'InheritedRule']

OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_GRANT_KIND_VALUES: set[OfficeWikiPageShareGrantDtoGrantKind] = { 'DirectInvite', 'InheritedRule',  }

def check_office_wiki_page_share_grant_dto_grant_kind(value: str) -> OfficeWikiPageShareGrantDtoGrantKind:
    if value in OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_GRANT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_GRANT_KIND_VALUES!r}")
