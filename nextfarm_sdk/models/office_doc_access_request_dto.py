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






T = TypeVar("T", bound="OfficeDocAccessRequestDto")



@_attrs_define
class OfficeDocAccessRequestDto:
    

    can_resend_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    granted_level: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    message: None | str | Unset = UNSET
    page_id: UUID | Unset = UNSET
    page_title: None | str | Unset = UNSET
    requested_level: None | str | Unset = UNSET
    requester_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        can_resend_at: None | str | Unset
        if isinstance(self.can_resend_at, Unset):
            can_resend_at = UNSET
        elif isinstance(self.can_resend_at, datetime.datetime):
            can_resend_at = self.can_resend_at.isoformat()
        else:
            can_resend_at = self.can_resend_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        granted_level: None | str | Unset
        if isinstance(self.granted_level, Unset):
            granted_level = UNSET
        else:
            granted_level = self.granted_level

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        page_id: str | Unset = UNSET
        if not isinstance(self.page_id, Unset):
            page_id = str(self.page_id)

        page_title: None | str | Unset
        if isinstance(self.page_title, Unset):
            page_title = UNSET
        else:
            page_title = self.page_title

        requested_level: None | str | Unset
        if isinstance(self.requested_level, Unset):
            requested_level = UNSET
        else:
            requested_level = self.requested_level

        requester_id: str | Unset = UNSET
        if not isinstance(self.requester_id, Unset):
            requester_id = str(self.requester_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_resend_at is not UNSET:
            field_dict["canResendAt"] = can_resend_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if decided_at is not UNSET:
            field_dict["decidedAt"] = decided_at
        if granted_level is not UNSET:
            field_dict["grantedLevel"] = granted_level
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if page_id is not UNSET:
            field_dict["pageId"] = page_id
        if page_title is not UNSET:
            field_dict["pageTitle"] = page_title
        if requested_level is not UNSET:
            field_dict["requestedLevel"] = requested_level
        if requester_id is not UNSET:
            field_dict["requesterId"] = requester_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_can_resend_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                can_resend_at_type_0 = datetime.datetime.fromisoformat(data)



                return can_resend_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        can_resend_at = _parse_can_resend_at(d.pop("canResendAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_decided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = datetime.datetime.fromisoformat(data)



                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        decided_at = _parse_decided_at(d.pop("decidedAt", UNSET))


        def _parse_granted_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        granted_level = _parse_granted_level(d.pop("grantedLevel", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        _page_id = d.pop("pageId", UNSET)
        page_id: UUID | Unset
        if isinstance(_page_id,  Unset):
            page_id = UNSET
        else:
            page_id = UUID(_page_id)




        def _parse_page_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_title = _parse_page_title(d.pop("pageTitle", UNSET))


        def _parse_requested_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_level = _parse_requested_level(d.pop("requestedLevel", UNSET))


        _requester_id = d.pop("requesterId", UNSET)
        requester_id: UUID | Unset
        if isinstance(_requester_id,  Unset):
            requester_id = UNSET
        else:
            requester_id = UUID(_requester_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_doc_access_request_dto = cls(
            can_resend_at=can_resend_at,
            created_at=created_at,
            decided_at=decided_at,
            granted_level=granted_level,
            id=id,
            message=message,
            page_id=page_id,
            page_title=page_title,
            requested_level=requested_level,
            requester_id=requester_id,
            status=status,
        )

        return office_doc_access_request_dto

