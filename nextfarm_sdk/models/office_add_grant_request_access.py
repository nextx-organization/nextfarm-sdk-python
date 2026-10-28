from typing import Literal

OfficeAddGrantRequestAccess = Literal['Edit', 'Read']

OFFICE_ADD_GRANT_REQUEST_ACCESS_VALUES: set[OfficeAddGrantRequestAccess] = { 'Edit', 'Read',  }

def check_office_add_grant_request_access(value: str) -> OfficeAddGrantRequestAccess:
    if value in OFFICE_ADD_GRANT_REQUEST_ACCESS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_ADD_GRANT_REQUEST_ACCESS_VALUES!r}")
