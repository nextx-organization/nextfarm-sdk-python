from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeMoveFolderRequest")



@_attrs_define
class OfficeMoveFolderRequest:
    

    new_parent_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        new_parent_id: None | str | Unset
        if isinstance(self.new_parent_id, Unset):
            new_parent_id = UNSET
        elif isinstance(self.new_parent_id, UUID):
            new_parent_id = str(self.new_parent_id)
        else:
            new_parent_id = self.new_parent_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if new_parent_id is not UNSET:
            field_dict["newParentId"] = new_parent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_new_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_parent_id_type_0 = UUID(data)



                return new_parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        new_parent_id = _parse_new_parent_id(d.pop("newParentId", UNSET))


        office_move_folder_request = cls(
            new_parent_id=new_parent_id,
        )

        return office_move_folder_request

