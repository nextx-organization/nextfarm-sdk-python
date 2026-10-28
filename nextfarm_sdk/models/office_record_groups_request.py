from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_record_filter import OfficeRecordFilter
  from ..models.office_record_sort import OfficeRecordSort





T = TypeVar("T", bound="OfficeRecordGroupsRequest")



@_attrs_define
class OfficeRecordGroupsRequest:
    

    filter_: OfficeRecordFilter | Unset = UNSET
    group_field_id: None | str | Unset = UNSET
    sort: list[OfficeRecordSort] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        from ..models.office_record_sort import OfficeRecordSort # noqa: PLC0415
        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        group_field_id: None | str | Unset
        if isinstance(self.group_field_id, Unset):
            group_field_id = UNSET
        else:
            group_field_id = self.group_field_id

        sort: list[dict[str, Any]] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, list):
            sort = []
            for sort_type_0_item_data in self.sort:
                sort_type_0_item = sort_type_0_item_data.to_dict()
                sort.append(sort_type_0_item)


        else:
            sort = self.sort


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if group_field_id is not UNSET:
            field_dict["groupFieldId"] = group_field_id
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        from ..models.office_record_sort import OfficeRecordSort # noqa: PLC0415
        d = dict(src_dict)
        _filter_ = d.pop("filter", UNSET)
        filter_: OfficeRecordFilter | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = OfficeRecordFilter.from_dict(_filter_)




        def _parse_group_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_field_id = _parse_group_field_id(d.pop("groupFieldId", UNSET))


        def _parse_sort(data: object) -> list[OfficeRecordSort] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_type_0 = []
                _sort_type_0 = data
                for sort_type_0_item_data in (_sort_type_0):
                    sort_type_0_item = OfficeRecordSort.from_dict(sort_type_0_item_data)



                    sort_type_0.append(sort_type_0_item)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRecordSort] | None | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))


        office_record_groups_request = cls(
            filter_=filter_,
            group_field_id=group_field_id,
            sort=sort,
        )

        return office_record_groups_request

