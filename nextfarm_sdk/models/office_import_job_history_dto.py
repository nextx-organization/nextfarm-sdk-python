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






T = TypeVar("T", bound="OfficeImportJobHistoryDto")



@_attrs_define
class OfficeImportJobHistoryDto:
    

    completed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    failed_rows: int | Unset = UNSET
    has_error_file: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    import_type: None | str | Unset = UNSET
    processed_rows: int | Unset = UNSET
    status: None | str | Unset = UNSET
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

        processed_rows = self.processed_rows

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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
        if failed_rows is not UNSET:
            field_dict["failedRows"] = failed_rows
        if has_error_file is not UNSET:
            field_dict["hasErrorFile"] = has_error_file
        if id is not UNSET:
            field_dict["id"] = id
        if import_type is not UNSET:
            field_dict["importType"] = import_type
        if processed_rows is not UNSET:
            field_dict["processedRows"] = processed_rows
        if status is not UNSET:
            field_dict["status"] = status
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


        processed_rows = d.pop("processedRows", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_total_rows(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_rows = _parse_total_rows(d.pop("totalRows", UNSET))


        office_import_job_history_dto = cls(
            completed_at=completed_at,
            created_at=created_at,
            failed_rows=failed_rows,
            has_error_file=has_error_file,
            id=id,
            import_type=import_type,
            processed_rows=processed_rows,
            status=status,
            total_rows=total_rows,
        )

        return office_import_job_history_dto

