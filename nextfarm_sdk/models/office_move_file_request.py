from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeMoveFileRequest")



@_attrs_define
class OfficeMoveFileRequest:
    

    target_folder_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        target_folder_id: str | Unset = UNSET
        if not isinstance(self.target_folder_id, Unset):
            target_folder_id = str(self.target_folder_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if target_folder_id is not UNSET:
            field_dict["targetFolderId"] = target_folder_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_folder_id = d.pop("targetFolderId", UNSET)
        target_folder_id: UUID | Unset
        if isinstance(_target_folder_id,  Unset):
            target_folder_id = UNSET
        else:
            target_folder_id = UUID(_target_folder_id)




        office_move_file_request = cls(
            target_folder_id=target_folder_id,
        )

        return office_move_file_request

