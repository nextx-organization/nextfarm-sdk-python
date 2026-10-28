from typing import Literal

OfficeDocNodeDtoDisplayMode = Literal['List', 'Tree']

OFFICE_DOC_NODE_DTO_DISPLAY_MODE_VALUES: set[OfficeDocNodeDtoDisplayMode] = { 'List', 'Tree',  }

def check_office_doc_node_dto_display_mode(value: str) -> OfficeDocNodeDtoDisplayMode:
    if value in OFFICE_DOC_NODE_DTO_DISPLAY_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_DTO_DISPLAY_MODE_VALUES!r}")
