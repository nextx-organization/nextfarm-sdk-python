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
  from ..models.office_upload_ticket_request_item import OfficeUploadTicketRequestItem





T = TypeVar("T", bound="OfficeCreateAttachmentUploadTicketsRequest")



@_attrs_define
class OfficeCreateAttachmentUploadTicketsRequest:
    

    entity_id: UUID | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    files: list[OfficeUploadTicketRequestItem] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_upload_ticket_request_item import OfficeUploadTicketRequestItem # noqa: PLC0415
        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        files: list[dict[str, Any]] | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_dict()
                files.append(files_type_0_item)


        else:
            files = self.files


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_upload_ticket_request_item import OfficeUploadTicketRequestItem # noqa: PLC0415
        d = dict(src_dict)
        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entityType", UNSET))


        def _parse_files(data: object) -> list[OfficeUploadTicketRequestItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in (_files_type_0):
                    files_type_0_item = OfficeUploadTicketRequestItem.from_dict(files_type_0_item_data)



                    files_type_0.append(files_type_0_item)

                return files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeUploadTicketRequestItem] | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))


        office_create_attachment_upload_tickets_request = cls(
            entity_id=entity_id,
            entity_type=entity_type,
            files=files,
        )

        return office_create_attachment_upload_tickets_request

