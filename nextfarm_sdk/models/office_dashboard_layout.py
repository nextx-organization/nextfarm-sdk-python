from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_dashboard_filter_def import OfficeDashboardFilterDef
  from ..models.office_dashboard_widget import OfficeDashboardWidget





T = TypeVar("T", bound="OfficeDashboardLayout")



@_attrs_define
class OfficeDashboardLayout:
    

    filters: list[OfficeDashboardFilterDef] | None | Unset = UNSET
    widgets: list[OfficeDashboardWidget] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_filter_def import OfficeDashboardFilterDef # noqa: PLC0415
        from ..models.office_dashboard_widget import OfficeDashboardWidget # noqa: PLC0415
        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)


        else:
            filters = self.filters

        widgets: list[dict[str, Any]] | None | Unset
        if isinstance(self.widgets, Unset):
            widgets = UNSET
        elif isinstance(self.widgets, list):
            widgets = []
            for widgets_type_0_item_data in self.widgets:
                widgets_type_0_item = widgets_type_0_item_data.to_dict()
                widgets.append(widgets_type_0_item)


        else:
            widgets = self.widgets


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if filters is not UNSET:
            field_dict["filters"] = filters
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_filter_def import OfficeDashboardFilterDef # noqa: PLC0415
        from ..models.office_dashboard_widget import OfficeDashboardWidget # noqa: PLC0415
        d = dict(src_dict)
        def _parse_filters(data: object) -> list[OfficeDashboardFilterDef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in (_filters_type_0):
                    filters_type_0_item = OfficeDashboardFilterDef.from_dict(filters_type_0_item_data)



                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardFilterDef] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))


        def _parse_widgets(data: object) -> list[OfficeDashboardWidget] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                widgets_type_0 = []
                _widgets_type_0 = data
                for widgets_type_0_item_data in (_widgets_type_0):
                    widgets_type_0_item = OfficeDashboardWidget.from_dict(widgets_type_0_item_data)



                    widgets_type_0.append(widgets_type_0_item)

                return widgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeDashboardWidget] | None | Unset, data)

        widgets = _parse_widgets(d.pop("widgets", UNSET))


        office_dashboard_layout = cls(
            filters=filters,
            widgets=widgets,
        )

        return office_dashboard_layout

