from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GisLifeStageDto")



@_attrs_define
class GisLifeStageDto:
    

    code: None | str | Unset = UNSET
    from_year: int | Unset = UNSET
    name: None | str | Unset = UNSET
    to_year: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        from_year = self.from_year

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        to_year: int | None | Unset
        if isinstance(self.to_year, Unset):
            to_year = UNSET
        else:
            to_year = self.to_year


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if from_year is not UNSET:
            field_dict["from_year"] = from_year
        if name is not UNSET:
            field_dict["name"] = name
        if to_year is not UNSET:
            field_dict["to_year"] = to_year

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        from_year = d.pop("from_year", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_to_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        to_year = _parse_to_year(d.pop("to_year", UNSET))


        gis_life_stage_dto = cls(
            code=code,
            from_year=from_year,
            name=name,
            to_year=to_year,
        )

        return gis_life_stage_dto

