from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisCropTypeListItemDto")



@_attrs_define
class GisCropTypeListItemDto:
    

    bearing_age_years: int | None | Unset = UNSET
    category: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    effective_lifecycle: None | str | Unset = UNSET
    grow_days: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    lifecycle: None | str | Unset = UNSET
    lifecycle_guessed: bool | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        bearing_age_years: int | None | Unset
        if isinstance(self.bearing_age_years, Unset):
            bearing_age_years = UNSET
        else:
            bearing_age_years = self.bearing_age_years

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        effective_lifecycle: None | str | Unset
        if isinstance(self.effective_lifecycle, Unset):
            effective_lifecycle = UNSET
        else:
            effective_lifecycle = self.effective_lifecycle

        grow_days: int | None | Unset
        if isinstance(self.grow_days, Unset):
            grow_days = UNSET
        else:
            grow_days = self.grow_days

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_active = self.is_active

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = self.lifecycle

        lifecycle_guessed = self.lifecycle_guessed

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if bearing_age_years is not UNSET:
            field_dict["bearing_age_years"] = bearing_age_years
        if category is not UNSET:
            field_dict["category"] = category
        if code is not UNSET:
            field_dict["code"] = code
        if effective_lifecycle is not UNSET:
            field_dict["effective_lifecycle"] = effective_lifecycle
        if grow_days is not UNSET:
            field_dict["grow_days"] = grow_days
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if lifecycle_guessed is not UNSET:
            field_dict["lifecycle_guessed"] = lifecycle_guessed
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_bearing_age_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bearing_age_years = _parse_bearing_age_years(d.pop("bearing_age_years", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_effective_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_lifecycle = _parse_effective_lifecycle(d.pop("effective_lifecycle", UNSET))


        def _parse_grow_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grow_days = _parse_grow_days(d.pop("grow_days", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_active = d.pop("is_active", UNSET)

        def _parse_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))


        lifecycle_guessed = d.pop("lifecycle_guessed", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        gis_crop_type_list_item_dto = cls(
            bearing_age_years=bearing_age_years,
            category=category,
            code=code,
            effective_lifecycle=effective_lifecycle,
            grow_days=grow_days,
            id=id,
            is_active=is_active,
            lifecycle=lifecycle,
            lifecycle_guessed=lifecycle_guessed,
            name=name,
        )

        return gis_crop_type_list_item_dto

