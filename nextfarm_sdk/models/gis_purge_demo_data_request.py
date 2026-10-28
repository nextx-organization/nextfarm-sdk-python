from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="GisPurgeDemoDataRequest")



@_attrs_define
class GisPurgeDemoDataRequest:
    

    batch_id: UUID | Unset = UNSET
    include_user_created: bool | Unset = UNSET
    workspace_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        batch_id: str | Unset = UNSET
        if not isinstance(self.batch_id, Unset):
            batch_id = str(self.batch_id)

        include_user_created = self.include_user_created

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if include_user_created is not UNSET:
            field_dict["include_user_created"] = include_user_created
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _batch_id = d.pop("batch_id", UNSET)
        batch_id: UUID | Unset
        if isinstance(_batch_id,  Unset):
            batch_id = UNSET
        else:
            batch_id = UUID(_batch_id)




        include_user_created = d.pop("include_user_created", UNSET)

        _workspace_id = d.pop("workspace_id", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        gis_purge_demo_data_request = cls(
            batch_id=batch_id,
            include_user_created=include_user_created,
            workspace_id=workspace_id,
        )

        return gis_purge_demo_data_request

