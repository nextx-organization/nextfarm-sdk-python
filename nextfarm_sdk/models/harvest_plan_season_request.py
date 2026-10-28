from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="HarvestPlanSeasonRequest")



@_attrs_define
class HarvestPlanSeasonRequest:
    

    season_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        season_id: str | Unset = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if season_id is not UNSET:
            field_dict["season_id"] = season_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _season_id = d.pop("season_id", UNSET)
        season_id: UUID | Unset
        if isinstance(_season_id,  Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)




        harvest_plan_season_request = cls(
            season_id=season_id,
        )

        return harvest_plan_season_request

