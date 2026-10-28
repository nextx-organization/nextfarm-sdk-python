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






T = TypeVar("T", bound="OfficeDataExportRequestDto")



@_attrs_define
class OfficeDataExportRequestDto:
    

    archive_size_bytes: int | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    download_url: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    exported_row_count: int | None | Unset = UNSET
    failure_reason_key: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    locale: None | str | Unset = UNSET
    requested_at: datetime.datetime | Unset = UNSET
    requested_by: UUID | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        archive_size_bytes: int | None | Unset
        if isinstance(self.archive_size_bytes, Unset):
            archive_size_bytes = UNSET
        else:
            archive_size_bytes = self.archive_size_bytes

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        download_url: None | str | Unset
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        exported_row_count: int | None | Unset
        if isinstance(self.exported_row_count, Unset):
            exported_row_count = UNSET
        else:
            exported_row_count = self.exported_row_count

        failure_reason_key: None | str | Unset
        if isinstance(self.failure_reason_key, Unset):
            failure_reason_key = UNSET
        else:
            failure_reason_key = self.failure_reason_key

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        requested_at: str | Unset = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        requested_by: str | Unset = UNSET
        if not isinstance(self.requested_by, Unset):
            requested_by = str(self.requested_by)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if archive_size_bytes is not UNSET:
            field_dict["archiveSizeBytes"] = archive_size_bytes
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if exported_row_count is not UNSET:
            field_dict["exportedRowCount"] = exported_row_count
        if failure_reason_key is not UNSET:
            field_dict["failureReasonKey"] = failure_reason_key
        if id is not UNSET:
            field_dict["id"] = id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if requested_at is not UNSET:
            field_dict["requestedAt"] = requested_at
        if requested_by is not UNSET:
            field_dict["requestedBy"] = requested_by
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_archive_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_size_bytes = _parse_archive_size_bytes(d.pop("archiveSizeBytes", UNSET))


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


        def _parse_download_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_url = _parse_download_url(d.pop("downloadUrl", UNSET))


        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        def _parse_exported_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exported_row_count = _parse_exported_row_count(d.pop("exportedRowCount", UNSET))


        def _parse_failure_reason_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason_key = _parse_failure_reason_key(d.pop("failureReasonKey", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))


        _requested_at = d.pop("requestedAt", UNSET)
        requested_at: datetime.datetime | Unset
        if isinstance(_requested_at,  Unset):
            requested_at = UNSET
        else:
            requested_at = datetime.datetime.fromisoformat(_requested_at)




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


        office_data_export_request_dto = cls(
            archive_size_bytes=archive_size_bytes,
            completed_at=completed_at,
            download_url=download_url,
            expires_at=expires_at,
            exported_row_count=exported_row_count,
            failure_reason_key=failure_reason_key,
            id=id,
            locale=locale,
            requested_at=requested_at,
            requested_by=requested_by,
            status=status,
        )

        return office_data_export_request_dto

