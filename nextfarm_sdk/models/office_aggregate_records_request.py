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
  from ..models.office_record_filter import OfficeRecordFilter





T = TypeVar("T", bound="OfficeAggregateRecordsRequest")



@_attrs_define
class OfficeAggregateRecordsRequest:
    

    field_ids: list[UUID] | None | Unset = UNSET
    filter_: OfficeRecordFilter | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        field_ids: list[str] | None | Unset
        if isinstance(self.field_ids, Unset):
            field_ids = UNSET
        elif isinstance(self.field_ids, list):
            field_ids = []
            for field_ids_type_0_item_data in self.field_ids:
                field_ids_type_0_item = str(field_ids_type_0_item_data)
                field_ids.append(field_ids_type_0_item)


        else:
            field_ids = self.field_ids

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if field_ids is not UNSET:
            field_dict["fieldIds"] = field_ids
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        d = dict(src_dict)
        def _parse_field_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_ids_type_0 = []
                _field_ids_type_0 = data
                for field_ids_type_0_item_data in (_field_ids_type_0):
                    field_ids_type_0_item = UUID(field_ids_type_0_item_data)



                    field_ids_type_0.append(field_ids_type_0_item)

                return field_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        field_ids = _parse_field_ids(d.pop("fieldIds", UNSET))


        _filter_ = d.pop("filter", UNSET)
        filter_: OfficeRecordFilter | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = OfficeRecordFilter.from_dict(_filter_)




        office_aggregate_records_request = cls(
            field_ids=field_ids,
            filter_=filter_,
        )

        return office_aggregate_records_request

