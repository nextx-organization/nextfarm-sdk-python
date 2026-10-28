from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeAddSharedWorkspaceRequest")



@_attrs_define
class OfficeAddSharedWorkspaceRequest:
    

    workspace_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        office_add_shared_workspace_request = cls(
            workspace_id=workspace_id,
        )

        return office_add_shared_workspace_request

