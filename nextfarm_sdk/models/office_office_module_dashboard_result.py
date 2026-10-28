from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_office_dashboard_widget import OfficeOfficeDashboardWidget





T = TypeVar("T", bound="OfficeOfficeModuleDashboardResult")



@_attrs_define
class OfficeOfficeModuleDashboardResult:
    

    failed: bool | Unset = UNSET
    module: None | str | Unset = UNSET
    widgets: list[OfficeOfficeDashboardWidget] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_office_dashboard_widget import OfficeOfficeDashboardWidget # noqa: PLC0415
        failed = self.failed

        module: None | str | Unset
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module

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
        if failed is not UNSET:
            field_dict["failed"] = failed
        if module is not UNSET:
            field_dict["module"] = module
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_office_dashboard_widget import OfficeOfficeDashboardWidget # noqa: PLC0415
        d = dict(src_dict)
        failed = d.pop("failed", UNSET)

        def _parse_module(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module = _parse_module(d.pop("module", UNSET))


        def _parse_widgets(data: object) -> list[OfficeOfficeDashboardWidget] | None | Unset:
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
                    widgets_type_0_item = OfficeOfficeDashboardWidget.from_dict(widgets_type_0_item_data)



                    widgets_type_0.append(widgets_type_0_item)

                return widgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOfficeDashboardWidget] | None | Unset, data)

        widgets = _parse_widgets(d.pop("widgets", UNSET))


        office_office_module_dashboard_result = cls(
            failed=failed,
            module=module,
            widgets=widgets,
        )

        return office_office_module_dashboard_result

