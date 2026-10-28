from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeRoleGrantDto")



@_attrs_define
class OfficeRoleGrantDto:
    

    access: None | str | Unset = UNSET
    column_fields: None | str | Unset = UNSET
    definition_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    role_id: UUID | Unset = UNSET
    row_rule: None | str | Unset = UNSET
    scope: None | str | Unset = UNSET
    table_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        access: None | str | Unset
        if isinstance(self.access, Unset):
            access = UNSET
        else:
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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        role_id: str | Unset = UNSET
        if not isinstance(self.role_id, Unset):
            role_id = str(self.role_id)

        row_rule: None | str | Unset
        if isinstance(self.row_rule, Unset):
            row_rule = UNSET
        else:
            row_rule = self.row_rule

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
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
        if id is not UNSET:
            field_dict["id"] = id
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
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
        def _parse_access(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access = _parse_access(d.pop("access", UNSET))


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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _role_id = d.pop("roleId", UNSET)
        role_id: UUID | Unset
        if isinstance(_role_id,  Unset):
            role_id = UNSET
        else:
            role_id = UUID(_role_id)




        def _parse_row_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        row_rule = _parse_row_rule(d.pop("rowRule", UNSET))


        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


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


        office_role_grant_dto = cls(
            access=access,
            column_fields=column_fields,
            definition_id=definition_id,
            id=id,
            role_id=role_id,
            row_rule=row_rule,
            scope=scope,
            table_id=table_id,
        )

        return office_role_grant_dto

