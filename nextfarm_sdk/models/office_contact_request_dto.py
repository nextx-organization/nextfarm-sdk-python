from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeContactRequestDto")



@_attrs_define
class OfficeContactRequestDto:
    

    created_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    requester_avatar_url: None | str | Unset = UNSET
    requester_name: None | str | Unset = UNSET
    requester_user_id: UUID | Unset = UNSET
    workspace_id: UUID | Unset = UNSET
    workspace_name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        requester_avatar_url: None | str | Unset
        if isinstance(self.requester_avatar_url, Unset):
            requester_avatar_url = UNSET
        else:
            requester_avatar_url = self.requester_avatar_url

        requester_name: None | str | Unset
        if isinstance(self.requester_name, Unset):
            requester_name = UNSET
        else:
            requester_name = self.requester_name

        requester_user_id: str | Unset = UNSET
        if not isinstance(self.requester_user_id, Unset):
            requester_user_id = str(self.requester_user_id)

        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        workspace_name: None | str | Unset
        if isinstance(self.workspace_name, Unset):
            workspace_name = UNSET
        else:
            workspace_name = self.workspace_name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if requester_avatar_url is not UNSET:
            field_dict["requesterAvatarUrl"] = requester_avatar_url
        if requester_name is not UNSET:
            field_dict["requesterName"] = requester_name
        if requester_user_id is not UNSET:
            field_dict["requesterUserId"] = requester_user_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_requester_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_avatar_url = _parse_requester_avatar_url(d.pop("requesterAvatarUrl", UNSET))


        def _parse_requester_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_name = _parse_requester_name(d.pop("requesterName", UNSET))


        _requester_user_id = d.pop("requesterUserId", UNSET)
        requester_user_id: UUID | Unset
        if isinstance(_requester_user_id,  Unset):
            requester_user_id = UNSET
        else:
            requester_user_id = UUID(_requester_user_id)




        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        def _parse_workspace_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_name = _parse_workspace_name(d.pop("workspaceName", UNSET))


        office_contact_request_dto = cls(
            created_at=created_at,
            id=id,
            requester_avatar_url=requester_avatar_url,
            requester_name=requester_name,
            requester_user_id=requester_user_id,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
        )

        return office_contact_request_dto

