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






T = TypeVar("T", bound="OfficeExportHistoryItemDto")



@_attrs_define
class OfficeExportHistoryItemDto:
    

    completed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    export_type: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    is_downloadable: bool | Unset = UNSET
    job_id: UUID | Unset = UNSET
    row_count: int | None | Unset = UNSET
    status: None | str | Unset = UNSET
    supported_formats: list[str] | None | Unset = UNSET





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

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        export_type: None | str | Unset
        if isinstance(self.export_type, Unset):
            export_type = UNSET
        else:
            export_type = self.export_type

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        is_downloadable = self.is_downloadable

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        supported_formats: list[str] | None | Unset
        if isinstance(self.supported_formats, Unset):
            supported_formats = UNSET
        elif isinstance(self.supported_formats, list):
            supported_formats = self.supported_formats


        else:
            supported_formats = self.supported_formats


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if export_type is not UNSET:
            field_dict["exportType"] = export_type
        if format_ is not UNSET:
            field_dict["format"] = format_
        if is_downloadable is not UNSET:
            field_dict["isDownloadable"] = is_downloadable
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if status is not UNSET:
            field_dict["status"] = status
        if supported_formats is not UNSET:
            field_dict["supportedFormats"] = supported_formats

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




        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)




        def _parse_export_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_type = _parse_export_type(d.pop("exportType", UNSET))


        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))


        is_downloadable = d.pop("isDownloadable", UNSET)

        _job_id = d.pop("jobId", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id,  Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)




        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("rowCount", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_supported_formats(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_formats_type_0 = cast(list[str], data)

                return supported_formats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_formats = _parse_supported_formats(d.pop("supportedFormats", UNSET))


        office_export_history_item_dto = cls(
            completed_at=completed_at,
            created_at=created_at,
            expires_at=expires_at,
            export_type=export_type,
            format_=format_,
            is_downloadable=is_downloadable,
            job_id=job_id,
            row_count=row_count,
            status=status,
            supported_formats=supported_formats,
        )

        return office_export_history_item_dto

