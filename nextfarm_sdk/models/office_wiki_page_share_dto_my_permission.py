from typing import Literal

OfficeWikiPageShareDtoMyPermission = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_WIKI_PAGE_SHARE_DTO_MY_PERMISSION_VALUES: set[OfficeWikiPageShareDtoMyPermission] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_wiki_page_share_dto_my_permission(value: str) -> OfficeWikiPageShareDtoMyPermission:
    if value in OFFICE_WIKI_PAGE_SHARE_DTO_MY_PERMISSION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_WIKI_PAGE_SHARE_DTO_MY_PERMISSION_VALUES!r}")
