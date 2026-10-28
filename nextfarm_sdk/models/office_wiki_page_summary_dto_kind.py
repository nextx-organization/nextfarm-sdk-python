from typing import Literal

OfficeWikiPageSummaryDtoKind = Literal['Doc', 'Sheet']

OFFICE_WIKI_PAGE_SUMMARY_DTO_KIND_VALUES: set[OfficeWikiPageSummaryDtoKind] = { 'Doc', 'Sheet',  }

def check_office_wiki_page_summary_dto_kind(value: str) -> OfficeWikiPageSummaryDtoKind:
    if value in OFFICE_WIKI_PAGE_SUMMARY_DTO_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_WIKI_PAGE_SUMMARY_DTO_KIND_VALUES!r}")
