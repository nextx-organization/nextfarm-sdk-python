from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeReorderFieldItemRequest")



@_attrs_define
class OfficeReorderFieldItemRequest:
    

    field_id: UUID | Unset = UNSET
    position: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_id: str | Unset = UNSET
        if not isinstance(self.field_id, Unset):
            field_id = str(self.field_id)

        position = self.position


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _field_id = d.pop("fieldId", UNSET)
        field_id: UUID | Unset
        if isinstance(_field_id,  Unset):
            field_id = UNSET
        else:
            field_id = UUID(_field_id)




        position = d.pop("position", UNSET)

        office_reorder_field_item_request = cls(
            field_id=field_id,
            position=position,
        )

        return office_reorder_field_item_request

