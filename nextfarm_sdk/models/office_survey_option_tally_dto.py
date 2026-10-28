from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeSurveyOptionTallyDto")



@_attrs_define
class OfficeSurveyOptionTallyDto:
    

    count: int | Unset = UNSET
    option: None | str | Unset = UNSET
    percentage: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        option: None | str | Unset
        if isinstance(self.option, Unset):
            option = UNSET
        else:
            option = self.option

        percentage = self.percentage


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if option is not UNSET:
            field_dict["option"] = option
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        option = _parse_option(d.pop("option", UNSET))


        percentage = d.pop("percentage", UNSET)

        office_survey_option_tally_dto = cls(
            count=count,
            option=option,
            percentage=percentage,
        )

        return office_survey_option_tally_dto

