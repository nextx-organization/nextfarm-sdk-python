from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_dashboard_filter_value import OfficeDashboardFilterValue





T = TypeVar("T", bound="OfficeWidgetDataRequest")



@_attrs_define
class OfficeWidgetDataRequest:
    

    filter_values: list[OfficeDashboardFilterValue] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_filter_value import OfficeDashboardFilterValue # noqa: PLC0415
        filter_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_values, Unset):
            filter_values = UNSET
        elif isinstance(self.filter_values, list):
            filter_values = []
            for filter_values_type_0_item_data in self.filter_values:
                filter_values_type_0_item = filter_values_type_0_item_data.to_dict()
                filter_values.append(filter_values_type_0_item)


        else:
            filter_values = self.filter_values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if filter_values is not UNSET:
            field_dict["filterValues"] = filter_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_filter_value import OfficeDashboardFilterValue # noqa: PLC0415
        d = dict(src_dict)
        def _parse_filter_values(data: object) -> list[OfficeDashboardFilterValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_values_type_0 = []
                _filter_values_type_0 = data
                for filter_values_type_0_item_data in (_filter_values_type_0):
                    filter_values_type_0_item = OfficeDashboardFilterValue.from_dict(filter_values_type_0_item_data)



                    filter_values_type_0.append(filter_values_type_0_item)

                return filter_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardFilterValue] | None | Unset, data)

        filter_values = _parse_filter_values(d.pop("filterValues", UNSET))


        office_widget_data_request = cls(
            filter_values=filter_values,
        )

        return office_widget_data_request

