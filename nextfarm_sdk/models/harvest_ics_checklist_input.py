from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_ics_checklist_item import HarvestIcsChecklistItem





T = TypeVar("T", bound="HarvestIcsChecklistInput")



@_attrs_define
class HarvestIcsChecklistInput:
    

    is_active: bool | Unset = UNSET
    items: list[HarvestIcsChecklistItem] | None | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_ics_checklist_item import HarvestIcsChecklistItem # noqa: PLC0415
        is_active = self.is_active

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if items is not UNSET:
            field_dict["items"] = items
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_ics_checklist_item import HarvestIcsChecklistItem # noqa: PLC0415
        d = dict(src_dict)
        is_active = d.pop("is_active", UNSET)

        def _parse_items(data: object) -> list[HarvestIcsChecklistItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = HarvestIcsChecklistItem.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestIcsChecklistItem] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        harvest_ics_checklist_input = cls(
            is_active=is_active,
            items=items,
            name=name,
        )

        return harvest_ics_checklist_input

