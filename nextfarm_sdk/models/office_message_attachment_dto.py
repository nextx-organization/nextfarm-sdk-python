from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_attachment_transcript_dto import OfficeAttachmentTranscriptDto





T = TypeVar("T", bound="OfficeMessageAttachmentDto")



@_attrs_define
class OfficeMessageAttachmentDto:
    

    content_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    has_thumbnail: bool | Unset = UNSET
    height: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    is_audio: bool | Unset = UNSET
    is_image: bool | Unset = UNSET
    relative_path: None | str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    transcript: OfficeAttachmentTranscriptDto | Unset = UNSET
    width: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_attachment_transcript_dto import OfficeAttachmentTranscriptDto # noqa: PLC0415
        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        has_thumbnail = self.has_thumbnail

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_audio = self.is_audio

        is_image = self.is_image

        relative_path: None | str | Unset
        if isinstance(self.relative_path, Unset):
            relative_path = UNSET
        else:
            relative_path = self.relative_path

        size_bytes = self.size_bytes

        transcript: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transcript, Unset):
            transcript = self.transcript.to_dict()

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
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if has_thumbnail is not UNSET:
            field_dict["hasThumbnail"] = has_thumbnail
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if is_audio is not UNSET:
            field_dict["isAudio"] = is_audio
        if is_image is not UNSET:
            field_dict["isImage"] = is_image
        if relative_path is not UNSET:
            field_dict["relativePath"] = relative_path
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_attachment_transcript_dto import OfficeAttachmentTranscriptDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


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




        is_audio = d.pop("isAudio", UNSET)

        is_image = d.pop("isImage", UNSET)

        def _parse_relative_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relative_path = _parse_relative_path(d.pop("relativePath", UNSET))


        size_bytes = d.pop("sizeBytes", UNSET)

        _transcript = d.pop("transcript", UNSET)
        transcript: OfficeAttachmentTranscriptDto | Unset
        if isinstance(_transcript,  Unset):
            transcript = UNSET
        else:
            transcript = OfficeAttachmentTranscriptDto.from_dict(_transcript)




        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))


        office_message_attachment_dto = cls(
            content_type=content_type,
            file_name=file_name,
            has_thumbnail=has_thumbnail,
            height=height,
            id=id,
            is_audio=is_audio,
            is_image=is_image,
            relative_path=relative_path,
            size_bytes=size_bytes,
            transcript=transcript,
            width=width,
        )

        return office_message_attachment_dto

