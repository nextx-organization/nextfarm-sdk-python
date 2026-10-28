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






T = TypeVar("T", bound="OfficeMomentDto")



@_attrs_define
class OfficeMomentDto:
    

    attachment_id: None | Unset | UUID = UNSET
    author_id: UUID | Unset = UNSET
    caption: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    has_thumbnail: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    is_viewed: bool | Unset = UNSET
    view_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        attachment_id: None | str | Unset
        if isinstance(self.attachment_id, Unset):
            attachment_id = UNSET
        elif isinstance(self.attachment_id, UUID):
            attachment_id = str(self.attachment_id)
        else:
            attachment_id = self.attachment_id

        author_id: str | Unset = UNSET
        if not isinstance(self.author_id, Unset):
            author_id = str(self.author_id)

        caption: None | str | Unset
        if isinstance(self.caption, Unset):
            caption = UNSET
        else:
            caption = self.caption

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        has_thumbnail = self.has_thumbnail

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_viewed = self.is_viewed

        view_count = self.view_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attachment_id is not UNSET:
            field_dict["attachmentId"] = attachment_id
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if caption is not UNSET:
            field_dict["caption"] = caption
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if has_thumbnail is not UNSET:
            field_dict["hasThumbnail"] = has_thumbnail
        if id is not UNSET:
            field_dict["id"] = id
        if is_viewed is not UNSET:
            field_dict["isViewed"] = is_viewed
        if view_count is not UNSET:
            field_dict["viewCount"] = view_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_attachment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                attachment_id_type_0 = UUID(data)



                return attachment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        attachment_id = _parse_attachment_id(d.pop("attachmentId", UNSET))


        _author_id = d.pop("authorId", UNSET)
        author_id: UUID | Unset
        if isinstance(_author_id,  Unset):
            author_id = UNSET
        else:
            author_id = UUID(_author_id)




        def _parse_caption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caption = _parse_caption(d.pop("caption", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        has_thumbnail = d.pop("hasThumbnail", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_viewed = d.pop("isViewed", UNSET)

        view_count = d.pop("viewCount", UNSET)

        office_moment_dto = cls(
            attachment_id=attachment_id,
            author_id=author_id,
            caption=caption,
            created_at=created_at,
            expires_at=expires_at,
            has_thumbnail=has_thumbnail,
            id=id,
            is_viewed=is_viewed,
            view_count=view_count,
        )

        return office_moment_dto

