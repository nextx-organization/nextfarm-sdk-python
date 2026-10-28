from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_dashboard_layout import OfficeDashboardLayout





T = TypeVar("T", bound="OfficeUpdateDashboardRequest")



@_attrs_define
class OfficeUpdateDashboardRequest:
    

    layout: OfficeDashboardLayout | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_layout import OfficeDashboardLayout # noqa: PLC0415
        layout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if layout is not UNSET:
            field_dict["layout"] = layout
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_layout import OfficeDashboardLayout # noqa: PLC0415
        d = dict(src_dict)
        _layout = d.pop("layout", UNSET)
        layout: OfficeDashboardLayout | Unset
        if isinstance(_layout,  Unset):
            layout = UNSET
        else:
            layout = OfficeDashboardLayout.from_dict(_layout)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_update_dashboard_request = cls(
            layout=layout,
            name=name,
        )

        return office_update_dashboard_request

