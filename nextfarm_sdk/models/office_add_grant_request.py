from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_add_grant_request_access import check_office_add_grant_request_access
from ..models.office_add_grant_request_access import OfficeAddGrantRequestAccess
from ..models.office_add_grant_request_scope import check_office_add_grant_request_scope
from ..models.office_add_grant_request_scope import OfficeAddGrantRequestScope
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAddGrantRequest")



@_attrs_define
class OfficeAddGrantRequest:
    

    access: OfficeAddGrantRequestAccess | Unset = UNSET
    column_fields: None | str | Unset = UNSET
    definition_id: None | Unset | UUID = UNSET
    row_rule: None | str | Unset = UNSET
    scope: OfficeAddGrantRequestScope | Unset = UNSET
    table_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        access: str | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access


        column_fields: None | str | Unset
        if isinstance(self.column_fields, Unset):
            column_fields = UNSET
        else:
            column_fields = self.column_fields

        definition_id: None | str | Unset
        if isinstance(self.definition_id, Unset):
            definition_id = UNSET
        elif isinstance(self.definition_id, UUID):
            definition_id = str(self.definition_id)
        else:
            definition_id = self.definition_id

        row_rule: None | str | Unset
        if isinstance(self.row_rule, Unset):
            row_rule = UNSET
        else:
            row_rule = self.row_rule

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope


        table_id: None | str | Unset
        if isinstance(self.table_id, Unset):
            table_id = UNSET
        elif isinstance(self.table_id, UUID):
            table_id = str(self.table_id)
        else:
            table_id = self.table_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if access is not UNSET:
            field_dict["access"] = access
        if column_fields is not UNSET:
            field_dict["columnFields"] = column_fields
        if definition_id is not UNSET:
            field_dict["definitionId"] = definition_id
        if row_rule is not UNSET:
            field_dict["rowRule"] = row_rule
        if scope is not UNSET:
            field_dict["scope"] = scope
        if table_id is not UNSET:
            field_dict["tableId"] = table_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _access = d.pop("access", UNSET)
        access: OfficeAddGrantRequestAccess | Unset
        if isinstance(_access,  Unset):
            access = UNSET
        else:
            access = check_office_add_grant_request_access(_access)




        def _parse_column_fields(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        column_fields = _parse_column_fields(d.pop("columnFields", UNSET))


        def _parse_definition_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                definition_id_type_0 = UUID(data)



                return definition_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        definition_id = _parse_definition_id(d.pop("definitionId", UNSET))


        def _parse_row_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        row_rule = _parse_row_rule(d.pop("rowRule", UNSET))


        _scope = d.pop("scope", UNSET)
        scope: OfficeAddGrantRequestScope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = check_office_add_grant_request_scope(_scope)




        def _parse_table_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                table_id_type_0 = UUID(data)



                return table_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        table_id = _parse_table_id(d.pop("tableId", UNSET))


        office_add_grant_request = cls(
            access=access,
            column_fields=column_fields,
            definition_id=definition_id,
            row_rule=row_rule,
            scope=scope,
            table_id=table_id,
        )

        return office_add_grant_request

