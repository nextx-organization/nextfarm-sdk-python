from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GisImportParcelError")



@_attrs_define
class GisImportParcelError:
    

    parcel_code: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    row_index: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        parcel_code: None | str | Unset
        if isinstance(self.parcel_code, Unset):
            parcel_code = UNSET
        else:
            parcel_code = self.parcel_code

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        row_index = self.row_index


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if parcel_code is not UNSET:
            field_dict["parcel_code"] = parcel_code
        if reason is not UNSET:
            field_dict["reason"] = reason
        if row_index is not UNSET:
            field_dict["row_index"] = row_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_parcel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parcel_code = _parse_parcel_code(d.pop("parcel_code", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        row_index = d.pop("row_index", UNSET)

        gis_import_parcel_error = cls(
            parcel_code=parcel_code,
            reason=reason,
            row_index=row_index,
        )

        return gis_import_parcel_error

