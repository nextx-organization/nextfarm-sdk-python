from typing import Literal

OfficeDocNodeShareGrantDtoPrincipalType = Literal['Department', 'Group', 'Guest', 'User']

OFFICE_DOC_NODE_SHARE_GRANT_DTO_PRINCIPAL_TYPE_VALUES: set[OfficeDocNodeShareGrantDtoPrincipalType] = { 'Department', 'Group', 'Guest', 'User',  }

def check_office_doc_node_share_grant_dto_principal_type(value: str) -> OfficeDocNodeShareGrantDtoPrincipalType:
    if value in OFFICE_DOC_NODE_SHARE_GRANT_DTO_PRINCIPAL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_DOC_NODE_SHARE_GRANT_DTO_PRINCIPAL_TYPE_VALUES!r}")
