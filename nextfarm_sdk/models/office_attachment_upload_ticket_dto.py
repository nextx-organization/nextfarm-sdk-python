from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_upload_ticket_dto import OfficeUploadTicketDto





T = TypeVar("T", bound="OfficeAttachmentUploadTicketDto")



@_attrs_define
class OfficeAttachmentUploadTicketDto:
    

    file: OfficeUploadTicketDto | Unset = UNSET
    thumbnail: OfficeUploadTicketDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_upload_ticket_dto import OfficeUploadTicketDto # noqa: PLC0415
        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if file is not UNSET:
            field_dict["file"] = file
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_upload_ticket_dto import OfficeUploadTicketDto # noqa: PLC0415
        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: OfficeUploadTicketDto | Unset
        if isinstance(_file,  Unset):
            file = UNSET
        else:
            file = OfficeUploadTicketDto.from_dict(_file)




        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: OfficeUploadTicketDto | Unset
        if isinstance(_thumbnail,  Unset):
            thumbnail = UNSET
        else:
            thumbnail = OfficeUploadTicketDto.from_dict(_thumbnail)




        office_attachment_upload_ticket_dto = cls(
            file=file,
            thumbnail=thumbnail,
        )

        return office_attachment_upload_ticket_dto

