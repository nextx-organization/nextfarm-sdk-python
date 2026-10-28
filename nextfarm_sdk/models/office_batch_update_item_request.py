from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeBatchUpdateItemRequest")



@_attrs_define
class OfficeBatchUpdateItemRequest:
    

    data: Any | Unset = UNSET
    id: UUID | Unset = UNSET
    replace: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        data = self.data

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        replace = self.replace


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if replace is not UNSET:
            field_dict["replace"] = replace

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        replace = d.pop("replace", UNSET)

        office_batch_update_item_request = cls(
            data=data,
            id=id,
            replace=replace,
        )

        return office_batch_update_item_request

