from typing import Literal

OfficeCreateDocNodeRequestDisplayMode = Literal['List', 'Tree']

OFFICE_CREATE_DOC_NODE_REQUEST_DISPLAY_MODE_VALUES: set[OfficeCreateDocNodeRequestDisplayMode] = { 'List', 'Tree',  }

def check_office_create_doc_node_request_display_mode(value: str) -> OfficeCreateDocNodeRequestDisplayMode:
    if value in OFFICE_CREATE_DOC_NODE_REQUEST_DISPLAY_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_CREATE_DOC_NODE_REQUEST_DISPLAY_MODE_VALUES!r}")
