from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestSprayRequest")



@_attrs_define
class HarvestSprayRequest:
    

    active_ingredient: None | str | Unset = UNSET
    pre_harvest_interval_days: int | None | Unset = UNSET
    product_name: None | str | Unset = UNSET
    worker_badge_codes: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active_ingredient: None | str | Unset
        if isinstance(self.active_ingredient, Unset):
            active_ingredient = UNSET
        else:
            active_ingredient = self.active_ingredient

        pre_harvest_interval_days: int | None | Unset
        if isinstance(self.pre_harvest_interval_days, Unset):
            pre_harvest_interval_days = UNSET
        else:
            pre_harvest_interval_days = self.pre_harvest_interval_days

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        worker_badge_codes: list[str] | None | Unset
        if isinstance(self.worker_badge_codes, Unset):
            worker_badge_codes = UNSET
        elif isinstance(self.worker_badge_codes, list):
            worker_badge_codes = self.worker_badge_codes


        else:
            worker_badge_codes = self.worker_badge_codes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active_ingredient is not UNSET:
            field_dict["active_ingredient"] = active_ingredient
        if pre_harvest_interval_days is not UNSET:
            field_dict["pre_harvest_interval_days"] = pre_harvest_interval_days
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if worker_badge_codes is not UNSET:
            field_dict["worker_badge_codes"] = worker_badge_codes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_active_ingredient(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_ingredient = _parse_active_ingredient(d.pop("active_ingredient", UNSET))


        def _parse_pre_harvest_interval_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pre_harvest_interval_days = _parse_pre_harvest_interval_days(d.pop("pre_harvest_interval_days", UNSET))


        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))


        def _parse_worker_badge_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                worker_badge_codes_type_0 = cast(list[str], data)

                return worker_badge_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        worker_badge_codes = _parse_worker_badge_codes(d.pop("worker_badge_codes", UNSET))


        harvest_spray_request = cls(
            active_ingredient=active_ingredient,
            pre_harvest_interval_days=pre_harvest_interval_days,
            product_name=product_name,
            worker_badge_codes=worker_badge_codes,
        )

        return harvest_spray_request

