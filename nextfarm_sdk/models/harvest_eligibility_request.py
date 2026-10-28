from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="HarvestEligibilityRequest")



@_attrs_define
class HarvestEligibilityRequest:
    

    farmer_ids: list[UUID] | None | Unset = UNSET
    on: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        farmer_ids: list[str] | None | Unset
        if isinstance(self.farmer_ids, Unset):
            farmer_ids = UNSET
        elif isinstance(self.farmer_ids, list):
            farmer_ids = []
            for farmer_ids_type_0_item_data in self.farmer_ids:
                farmer_ids_type_0_item = str(farmer_ids_type_0_item_data)
                farmer_ids.append(farmer_ids_type_0_item)


        else:
            farmer_ids = self.farmer_ids

        on: None | str | Unset
        if isinstance(self.on, Unset):
            on = UNSET
        elif isinstance(self.on, datetime.date):
            on = self.on.isoformat()
        else:
            on = self.on


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if farmer_ids is not UNSET:
            field_dict["farmer_ids"] = farmer_ids
        if on is not UNSET:
            field_dict["on"] = on

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_farmer_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                farmer_ids_type_0 = []
                _farmer_ids_type_0 = data
                for farmer_ids_type_0_item_data in (_farmer_ids_type_0):
                    farmer_ids_type_0_item = UUID(farmer_ids_type_0_item_data)



                    farmer_ids_type_0.append(farmer_ids_type_0_item)

                return farmer_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        farmer_ids = _parse_farmer_ids(d.pop("farmer_ids", UNSET))


        def _parse_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_type_0 = datetime.date.fromisoformat(data)



                return on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        on = _parse_on(d.pop("on", UNSET))


        harvest_eligibility_request = cls(
            farmer_ids=farmer_ids,
            on=on,
        )

        return harvest_eligibility_request

