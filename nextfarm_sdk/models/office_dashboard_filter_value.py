from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeDashboardFilterValue")



@_attrs_define
class OfficeDashboardFilterValue:
    

    filter_id: None | str | Unset = UNSET
    from_: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    to: None | str | Unset = UNSET
    values: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        filter_id: None | str | Unset
        if isinstance(self.filter_id, Unset):
            filter_id = UNSET
        else:
            filter_id = self.filter_id

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        values: list[str] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values


        else:
            values = self.values


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if filter_id is not UNSET:
            field_dict["filterId"] = filter_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if text is not UNSET:
            field_dict["text"] = text
        if to is not UNSET:
            field_dict["to"] = to
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_filter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_id = _parse_filter_id(d.pop("filterId", UNSET))


        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        def _parse_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        office_dashboard_filter_value = cls(
            filter_id=filter_id,
            from_=from_,
            text=text,
            to=to,
            values=values,
        )

        return office_dashboard_filter_value

