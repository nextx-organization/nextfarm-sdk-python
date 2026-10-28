from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_map_import_request_column_mapping_type_0 import OfficeMapImportRequestColumnMappingType0





T = TypeVar("T", bound="OfficeMapImportRequest")



@_attrs_define
class OfficeMapImportRequest:
    

    column_mapping: None | OfficeMapImportRequestColumnMappingType0 | Unset = UNSET
    match_key: None | str | Unset = UNSET
    upload_key: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_map_import_request_column_mapping_type_0 import OfficeMapImportRequestColumnMappingType0 # noqa: PLC0415
        column_mapping: dict[str, Any] | None | Unset
        if isinstance(self.column_mapping, Unset):
            column_mapping = UNSET
        elif isinstance(self.column_mapping, OfficeMapImportRequestColumnMappingType0):
            column_mapping = self.column_mapping.to_dict()
        else:
            column_mapping = self.column_mapping

        match_key: None | str | Unset
        if isinstance(self.match_key, Unset):
            match_key = UNSET
        else:
            match_key = self.match_key

        upload_key: None | str | Unset
        if isinstance(self.upload_key, Unset):
            upload_key = UNSET
        else:
            upload_key = self.upload_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if column_mapping is not UNSET:
            field_dict["columnMapping"] = column_mapping
        if match_key is not UNSET:
            field_dict["matchKey"] = match_key
        if upload_key is not UNSET:
            field_dict["uploadKey"] = upload_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_map_import_request_column_mapping_type_0 import OfficeMapImportRequestColumnMappingType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_column_mapping(data: object) -> None | OfficeMapImportRequestColumnMappingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                column_mapping_type_0 = OfficeMapImportRequestColumnMappingType0.from_dict(data)



                return column_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeMapImportRequestColumnMappingType0 | Unset, data)

        column_mapping = _parse_column_mapping(d.pop("columnMapping", UNSET))


        def _parse_match_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        match_key = _parse_match_key(d.pop("matchKey", UNSET))


        def _parse_upload_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_key = _parse_upload_key(d.pop("uploadKey", UNSET))


        office_map_import_request = cls(
            column_mapping=column_mapping,
            match_key=match_key,
            upload_key=upload_key,
        )

        return office_map_import_request

