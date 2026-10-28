from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCreateExportResultDto")



@_attrs_define
class OfficeCreateExportResultDto:
    

    download_url: None | str | Unset = UNSET
    export_type: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    is_sync: bool | Unset = UNSET
    job_id: UUID | Unset = UNSET
    scope: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    supported_formats: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        download_url: None | str | Unset
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url

        export_type: None | str | Unset
        if isinstance(self.export_type, Unset):
            export_type = UNSET
        else:
            export_type = self.export_type

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        is_sync = self.is_sync

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

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
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if export_type is not UNSET:
            field_dict["exportType"] = export_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if format_ is not UNSET:
            field_dict["format"] = format_
        if is_sync is not UNSET:
            field_dict["isSync"] = is_sync
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if status is not UNSET:
            field_dict["status"] = status
        if supported_formats is not UNSET:
            field_dict["supportedFormats"] = supported_formats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_download_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_url = _parse_download_url(d.pop("downloadUrl", UNSET))


        def _parse_export_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_type = _parse_export_type(d.pop("exportType", UNSET))


        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))


        is_sync = d.pop("isSync", UNSET)

        _job_id = d.pop("jobId", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id,  Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)




        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


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


        office_create_export_result_dto = cls(
            download_url=download_url,
            export_type=export_type,
            file_name=file_name,
            format_=format_,
            is_sync=is_sync,
            job_id=job_id,
            scope=scope,
            status=status,
            supported_formats=supported_formats,
        )

        return office_create_export_result_dto

