from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeBatchCreateRecordsRequest")



@_attrs_define
class OfficeBatchCreateRecordsRequest:
    

    records: list[Any] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        records: list[Any] | None | Unset
        if isinstance(self.records, Unset):
            records = UNSET
        elif isinstance(self.records, list):
            records = self.records


        else:
            records = self.records


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_records(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                records_type_0 = cast(list[Any], data)

                return records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        records = _parse_records(d.pop("records", UNSET))


        office_batch_create_records_request = cls(
            records=records,
        )

        return office_batch_create_records_request

