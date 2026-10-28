from typing import Literal

OfficeDocNodeDtoNodeType = Literal['Base', 'Doc', 'File', 'Folder', 'Form', 'Shortcut', 'Space']

OFFICE_DOC_NODE_DTO_NODE_TYPE_VALUES: set[OfficeDocNodeDtoNodeType] = { 'Base', 'Doc', 'File', 'Folder', 'Form', 'Shortcut', 'Space',  }

def check_office_doc_node_dto_node_type(value: str) -> OfficeDocNodeDtoNodeType:
    if value in OFFICE_DOC_NODE_DTO_NODE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_DTO_NODE_TYPE_VALUES!r}")
