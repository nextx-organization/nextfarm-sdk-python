from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTaskLinkInput")



@_attrs_define
class OfficeTaskLinkInput:
    

    entity_id: UUID | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        office_task_link_input = cls(
            entity_id=entity_id,
            entity_type=entity_type,
            label=label,
        )

        return office_task_link_input

