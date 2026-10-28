from typing import Literal

OfficeWikiPageDtoKind = Literal['Doc', 'Sheet']

OFFICE_WIKI_PAGE_DTO_KIND_VALUES: set[OfficeWikiPageDtoKind] = { 'Doc', 'Sheet',  }

def check_office_wiki_page_dto_kind(value: str) -> OfficeWikiPageDtoKind:
    if value in OFFICE_WIKI_PAGE_DTO_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_WIKI_PAGE_DTO_KIND_VALUES!r}")
