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






T = TypeVar("T", bound="OfficeImportJobDto")



@_attrs_define
class OfficeImportJobDto:
    

    completed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    error_message: None | str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    failed_rows: int | Unset = UNSET
    has_error_file: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    import_type: None | str | Unset = UNSET
    mode: None | str | Unset = UNSET
    processed_rows: int | Unset = UNSET
    requested_by: UUID | Unset = UNSET
    status: None | str | Unset = UNSET
    supports_undo: bool | Unset = UNSET
    total_rows: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        failed_rows = self.failed_rows

        has_error_file = self.has_error_file

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        import_type: None | str | Unset
        if isinstance(self.import_type, Unset):
            import_type = UNSET
        else:
            import_type = self.import_type

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        processed_rows = self.processed_rows

        requested_by: str | Unset = UNSET
        if not isinstance(self.requested_by, Unset):
            requested_by = str(self.requested_by)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        supports_undo = self.supports_undo

        total_rows: int | None | Unset
        if isinstance(self.total_rows, Unset):
            total_rows = UNSET
        else:
            total_rows = self.total_rows


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if failed_rows is not UNSET:
            field_dict["failedRows"] = failed_rows
        if has_error_file is not UNSET:
            field_dict["hasErrorFile"] = has_error_file
        if id is not UNSET:
            field_dict["id"] = id
        if import_type is not UNSET:
            field_dict["importType"] = import_type
        if mode is not UNSET:
            field_dict["mode"] = mode
        if processed_rows is not UNSET:
            field_dict["processedRows"] = processed_rows
        if requested_by is not UNSET:
            field_dict["requestedBy"] = requested_by
        if status is not UNSET:
            field_dict["status"] = status
        if supports_undo is not UNSET:
            field_dict["supportsUndo"] = supports_undo
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))


        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        failed_rows = d.pop("failedRows", UNSET)

        has_error_file = d.pop("hasErrorFile", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_import_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_type = _parse_import_type(d.pop("importType", UNSET))


        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        processed_rows = d.pop("processedRows", UNSET)

        _requested_by = d.pop("requestedBy", UNSET)
        requested_by: UUID | Unset
        if isinstance(_requested_by,  Unset):
            requested_by = UNSET
        else:
            requested_by = UUID(_requested_by)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        supports_undo = d.pop("supportsUndo", UNSET)

        def _parse_total_rows(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_rows = _parse_total_rows(d.pop("totalRows", UNSET))


        office_import_job_dto = cls(
            completed_at=completed_at,
            created_at=created_at,
            error_message=error_message,
            expires_at=expires_at,
            failed_rows=failed_rows,
            has_error_file=has_error_file,
            id=id,
            import_type=import_type,
            mode=mode,
            processed_rows=processed_rows,
            requested_by=requested_by,
            status=status,
            supports_undo=supports_undo,
            total_rows=total_rows,
        )

        return office_import_job_dto

