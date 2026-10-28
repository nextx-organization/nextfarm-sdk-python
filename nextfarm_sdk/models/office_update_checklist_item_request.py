from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeUpdateChecklistItemRequest")



@_attrs_define
class OfficeUpdateChecklistItemRequest:
    

    is_done: bool | None | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_done: bool | None | Unset
        if isinstance(self.is_done, Unset):
            is_done = UNSET
        else:
            is_done = self.is_done

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_done is not UNSET:
            field_dict["isDone"] = is_done
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_is_done(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_done = _parse_is_done(d.pop("isDone", UNSET))


        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sortOrder", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_update_checklist_item_request = cls(
            is_done=is_done,
            sort_order=sort_order,
            title=title,
        )

        return office_update_checklist_item_request

