from typing import Literal

OfficeDecideDocAccessRequestRequestGrantedLevel = Literal['Comment', 'Edit', 'Manage', 'View']

OFFICE_DECIDE_DOC_ACCESS_REQUEST_REQUEST_GRANTED_LEVEL_VALUES: set[OfficeDecideDocAccessRequestRequestGrantedLevel] = { 'Comment', 'Edit', 'Manage', 'View',  }

def check_office_decide_doc_access_request_request_granted_level(value: str) -> OfficeDecideDocAccessRequestRequestGrantedLevel:
    if value in OFFICE_DECIDE_DOC_ACCESS_REQUEST_REQUEST_GRANTED_LEVEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DECIDE_DOC_ACCESS_REQUEST_REQUEST_GRANTED_LEVEL_VALUES!r}")
