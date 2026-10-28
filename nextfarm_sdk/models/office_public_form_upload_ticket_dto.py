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
  from ..models.office_upload_ticket_dto import OfficeUploadTicketDto





T = TypeVar("T", bound="OfficePublicFormUploadTicketDto")



@_attrs_define
class OfficePublicFormUploadTicketDto:
    

    ticket: OfficeUploadTicketDto | Unset = UNSET
    upload_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_upload_ticket_dto import OfficeUploadTicketDto # noqa: PLC0415
        ticket: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ticket, Unset):
            ticket = self.ticket.to_dict()

        upload_id: str | Unset = UNSET
        if not isinstance(self.upload_id, Unset):
            upload_id = str(self.upload_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if upload_id is not UNSET:
            field_dict["uploadId"] = upload_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_upload_ticket_dto import OfficeUploadTicketDto # noqa: PLC0415
        d = dict(src_dict)
        _ticket = d.pop("ticket", UNSET)
        ticket: OfficeUploadTicketDto | Unset
        if isinstance(_ticket,  Unset):
            ticket = UNSET
        else:
            ticket = OfficeUploadTicketDto.from_dict(_ticket)




        _upload_id = d.pop("uploadId", UNSET)
        upload_id: UUID | Unset
        if isinstance(_upload_id,  Unset):
            upload_id = UNSET
        else:
            upload_id = UUID(_upload_id)




        office_public_form_upload_ticket_dto = cls(
            ticket=ticket,
            upload_id=upload_id,
        )

        return office_public_form_upload_ticket_dto

