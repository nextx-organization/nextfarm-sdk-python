from typing import Literal

OfficeTaskDocLinkDtoNodeType = Literal['Base', 'Doc', 'File', 'Folder', 'Form', 'Shortcut', 'Space']

OFFICE_TASK_DOC_LINK_DTO_NODE_TYPE_VALUES: set[OfficeTaskDocLinkDtoNodeType] = { 'Base', 'Doc', 'File', 'Folder', 'Form', 'Shortcut', 'Space',  }

def check_office_task_doc_link_dto_node_type(value: str) -> OfficeTaskDocLinkDtoNodeType:
    if value in OFFICE_TASK_DOC_LINK_DTO_NODE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_TASK_DOC_LINK_DTO_NODE_TYPE_VALUES!r}")
