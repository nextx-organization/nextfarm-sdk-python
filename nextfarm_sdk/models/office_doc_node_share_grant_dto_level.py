from typing import Literal

OfficeDocNodeShareGrantDtoLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_DOC_NODE_SHARE_GRANT_DTO_LEVEL_VALUES: set[OfficeDocNodeShareGrantDtoLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_doc_node_share_grant_dto_level(value: str) -> OfficeDocNodeShareGrantDtoLevel:
    if value in OFFICE_DOC_NODE_SHARE_GRANT_DTO_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_SHARE_GRANT_DTO_LEVEL_VALUES!r}")
