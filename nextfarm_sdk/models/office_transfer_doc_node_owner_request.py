from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeTransferDocNodeOwnerRequest")



@_attrs_define
class OfficeTransferDocNodeOwnerRequest:
    

    new_owner_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        new_owner_id: str | Unset = UNSET
        if not isinstance(self.new_owner_id, Unset):
            new_owner_id = str(self.new_owner_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if new_owner_id is not UNSET:
            field_dict["newOwnerId"] = new_owner_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _new_owner_id = d.pop("newOwnerId", UNSET)
        new_owner_id: UUID | Unset
        if isinstance(_new_owner_id,  Unset):
            new_owner_id = UNSET
        else:
            new_owner_id = UUID(_new_owner_id)




        office_transfer_doc_node_owner_request = cls(
            new_owner_id=new_owner_id,
        )

        return office_transfer_doc_node_owner_request

