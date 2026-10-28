from typing import Literal

OfficeAddGrantRequestScope = Literal['Approval', 'Base']

OFFICE_ADD_GRANT_REQUEST_SCOPE_VALUES: set[OfficeAddGrantRequestScope] = { 'Approval', 'Base',  }

def check_office_add_grant_request_scope(value: str) -> OfficeAddGrantRequestScope:
    if value in OFFICE_ADD_GRANT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_ADD_GRANT_REQUEST_SCOPE_VALUES!r}")
