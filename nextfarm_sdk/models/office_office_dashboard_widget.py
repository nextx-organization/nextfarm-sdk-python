from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_office_dashboard_widget_kind import check_office_office_dashboard_widget_kind
from ..models.office_office_dashboard_widget_kind import OfficeOfficeDashboardWidgetKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeOfficeDashboardWidget")



@_attrs_define
class OfficeOfficeDashboardWidget:
    

    key: None | str | Unset = UNSET
    kind: OfficeOfficeDashboardWidgetKind | Unset = UNSET
    label_key: None | str | Unset = UNSET
    module: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    value: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind


        label_key: None | str | Unset
        if isinstance(self.label_key, Unset):
            label_key = UNSET
        else:
            label_key = self.label_key

        module: None | str | Unset
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label_key is not UNSET:
            field_dict["labelKey"] = label_key
        if module is not UNSET:
            field_dict["module"] = module
        if url is not UNSET:
            field_dict["url"] = url
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        _kind = d.pop("kind", UNSET)
        kind: OfficeOfficeDashboardWidgetKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = check_office_office_dashboard_widget_kind(_kind)




        def _parse_label_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label_key = _parse_label_key(d.pop("labelKey", UNSET))


        def _parse_module(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module = _parse_module(d.pop("module", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        value = d.pop("value", UNSET)

        office_office_dashboard_widget = cls(
            key=key,
            kind=kind,
            label_key=label_key,
            module=module,
            url=url,
            value=value,
        )

        return office_office_dashboard_widget

