from typing import Literal

OfficeCreateDocNodeRequestNodeType = Literal['Base', 'Doc', 'File', 'Folder', 'Form', 'Shortcut', 'Space']

OFFICE_CREATE_DOC_NODE_REQUEST_NODE_TYPE_VALUES: set[OfficeCreateDocNodeRequestNodeType] = { 'Base', 'Doc', 'File', 'Folder', 'Form', 'Shortcut', 'Space',  }

def check_office_create_doc_node_request_node_type(value: str) -> OfficeCreateDocNodeRequestNodeType:
    if value in OFFICE_CREATE_DOC_NODE_REQUEST_NODE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_CREATE_DOC_NODE_REQUEST_NODE_TYPE_VALUES!r}")
