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

if TYPE_CHECKING:
  from ..models.office_chat_folder_dto import OfficeChatFolderDto





T = TypeVar("T", bound="OfficeChannelAttachmentDto")



@_attrs_define
class OfficeChannelAttachmentDto:
    

    content_type: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    file_name: None | str | Unset = UNSET
    folder: OfficeChatFolderDto | Unset = UNSET
    has_thumbnail: bool | Unset = UNSET
    height: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    in_thread: bool | Unset = UNSET
    is_image: bool | Unset = UNSET
    is_video: bool | Unset = UNSET
    kind: None | str | Unset = UNSET
    message_id: UUID | Unset = UNSET
    relative_path: None | str | Unset = UNSET
    sender_id: UUID | Unset = UNSET
    size_bytes: int | Unset = UNSET
    uploaded_at: datetime.datetime | Unset = UNSET
    uploaded_by: UUID | Unset = UNSET
    width: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_folder_dto import OfficeChatFolderDto # noqa: PLC0415
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        has_thumbnail = self.has_thumbnail

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        in_thread = self.in_thread

        is_image = self.is_image

        is_video = self.is_video

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        relative_path: None | str | Unset
        if isinstance(self.relative_path, Unset):
            relative_path = UNSET
        else:
            relative_path = self.relative_path

        sender_id: str | Unset = UNSET
        if not isinstance(self.sender_id, Unset):
            sender_id = str(self.sender_id)

        size_bytes = self.size_bytes

        uploaded_at: str | Unset = UNSET
        if not isinstance(self.uploaded_at, Unset):
            uploaded_at = self.uploaded_at.isoformat()

        uploaded_by: str | Unset = UNSET
        if not isinstance(self.uploaded_by, Unset):
            uploaded_by = str(self.uploaded_by)

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if folder is not UNSET:
            field_dict["folder"] = folder
        if has_thumbnail is not UNSET:
            field_dict["hasThumbnail"] = has_thumbnail
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if in_thread is not UNSET:
            field_dict["inThread"] = in_thread
        if is_image is not UNSET:
            field_dict["isImage"] = is_image
        if is_video is not UNSET:
            field_dict["isVideo"] = is_video
        if kind is not UNSET:
            field_dict["kind"] = kind
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if relative_path is not UNSET:
            field_dict["relativePath"] = relative_path
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if uploaded_at is not UNSET:
            field_dict["uploadedAt"] = uploaded_at
        if uploaded_by is not UNSET:
            field_dict["uploadedBy"] = uploaded_by
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_folder_dto import OfficeChatFolderDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        _folder = d.pop("folder", UNSET)
        folder: OfficeChatFolderDto | Unset
        if isinstance(_folder,  Unset):
            folder = UNSET
        else:
            folder = OfficeChatFolderDto.from_dict(_folder)




        has_thumbnail = d.pop("hasThumbnail", UNSET)

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        in_thread = d.pop("inThread", UNSET)

        is_image = d.pop("isImage", UNSET)

        is_video = d.pop("isVideo", UNSET)

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        def _parse_relative_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relative_path = _parse_relative_path(d.pop("relativePath", UNSET))


        _sender_id = d.pop("senderId", UNSET)
        sender_id: UUID | Unset
        if isinstance(_sender_id,  Unset):
            sender_id = UNSET
        else:
            sender_id = UUID(_sender_id)




        size_bytes = d.pop("sizeBytes", UNSET)

        _uploaded_at = d.pop("uploadedAt", UNSET)
        uploaded_at: datetime.datetime | Unset
        if isinstance(_uploaded_at,  Unset):
            uploaded_at = UNSET
        else:
            uploaded_at = datetime.datetime.fromisoformat(_uploaded_at)




        _uploaded_by = d.pop("uploadedBy", UNSET)
        uploaded_by: UUID | Unset
        if isinstance(_uploaded_by,  Unset):
            uploaded_by = UNSET
        else:
            uploaded_by = UUID(_uploaded_by)




        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))


        office_channel_attachment_dto = cls(
            content_type=content_type,
            created_at=created_at,
            file_name=file_name,
            folder=folder,
            has_thumbnail=has_thumbnail,
            height=height,
            id=id,
            in_thread=in_thread,
            is_image=is_image,
            is_video=is_video,
            kind=kind,
            message_id=message_id,
            relative_path=relative_path,
            sender_id=sender_id,
            size_bytes=size_bytes,
            uploaded_at=uploaded_at,
            uploaded_by=uploaded_by,
            width=width,
        )

        return office_channel_attachment_dto

