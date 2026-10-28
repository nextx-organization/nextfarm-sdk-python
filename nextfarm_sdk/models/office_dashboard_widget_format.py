from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeDashboardWidgetFormat")



@_attrs_define
class OfficeDashboardWidgetFormat:
    

    decimals: int | None | Unset = UNSET
    prefix: None | str | Unset = UNSET
    style: None | str | Unset = UNSET
    suffix: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        decimals: int | None | Unset
        if isinstance(self.decimals, Unset):
            decimals = UNSET
        else:
            decimals = self.decimals

        prefix: None | str | Unset
        if isinstance(self.prefix, Unset):
            prefix = UNSET
        else:
            prefix = self.prefix

        style: None | str | Unset
        if isinstance(self.style, Unset):
            style = UNSET
        else:
            style = self.style

        suffix: None | str | Unset
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if style is not UNSET:
            field_dict["style"] = style
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_decimals(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        decimals = _parse_decimals(d.pop("decimals", UNSET))


        def _parse_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefix = _parse_prefix(d.pop("prefix", UNSET))


        def _parse_style(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        style = _parse_style(d.pop("style", UNSET))


        def _parse_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))


        office_dashboard_widget_format = cls(
            decimals=decimals,
            prefix=prefix,
            style=style,
            suffix=suffix,
        )

        return office_dashboard_widget_format

