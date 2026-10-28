from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.harvest_plan_line_input import HarvestPlanLineInput





T = TypeVar("T", bound="HarvestPlanLinesRequest")



@_attrs_define
class HarvestPlanLinesRequest:
    

    lines: list[HarvestPlanLineInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.harvest_plan_line_input import HarvestPlanLineInput # noqa: PLC0415
        lines: list[dict[str, Any]] | None | Unset
        if isinstance(self.lines, Unset):
            lines = UNSET
        elif isinstance(self.lines, list):
            lines = []
            for lines_type_0_item_data in self.lines:
                lines_type_0_item = lines_type_0_item_data.to_dict()
                lines.append(lines_type_0_item)


        else:
            lines = self.lines


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harvest_plan_line_input import HarvestPlanLineInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_lines(data: object) -> list[HarvestPlanLineInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lines_type_0 = []
                _lines_type_0 = data
                for lines_type_0_item_data in (_lines_type_0):
                    lines_type_0_item = HarvestPlanLineInput.from_dict(lines_type_0_item_data)



                    lines_type_0.append(lines_type_0_item)

                return lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HarvestPlanLineInput] | None | Unset, data)

        lines = _parse_lines(d.pop("lines", UNSET))


        harvest_plan_lines_request = cls(
            lines=lines,
        )

        return harvest_plan_lines_request

