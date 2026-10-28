from typing import Literal

OfficeWikiPageShareGrantDtoLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_LEVEL_VALUES: set[OfficeWikiPageShareGrantDtoLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_wiki_page_share_grant_dto_level(value: str) -> OfficeWikiPageShareGrantDtoLevel:
    if value in OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_WIKI_PAGE_SHARE_GRANT_DTO_LEVEL_VALUES!r}")
