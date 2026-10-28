from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeSetCustomFieldValueRequest")



@_attrs_define
class OfficeSetCustomFieldValueRequest:
    

    custom_field_id: UUID | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        custom_field_id: str | Unset = UNSET
        if not isinstance(self.custom_field_id, Unset):
            custom_field_id = str(self.custom_field_id)

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if custom_field_id is not UNSET:
            field_dict["customFieldId"] = custom_field_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _custom_field_id = d.pop("customFieldId", UNSET)
        custom_field_id: UUID | Unset
        if isinstance(_custom_field_id,  Unset):
            custom_field_id = UNSET
        else:
            custom_field_id = UUID(_custom_field_id)




        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entityType", UNSET))


        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        office_set_custom_field_value_request = cls(
            custom_field_id=custom_field_id,
            entity_id=entity_id,
            entity_type=entity_type,
            value=value,
        )

        return office_set_custom_field_value_request

