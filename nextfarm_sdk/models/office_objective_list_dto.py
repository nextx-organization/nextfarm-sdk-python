from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_objective_dto import OfficeObjectiveDto
  from ..models.office_okr_summary_dto import OfficeOkrSummaryDto





T = TypeVar("T", bound="OfficeObjectiveListDto")



@_attrs_define
class OfficeObjectiveListDto:
    

    objectives: list[OfficeObjectiveDto] | None | Unset = UNSET
    summary: OfficeOkrSummaryDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_objective_dto import OfficeObjectiveDto # noqa: PLC0415
        from ..models.office_okr_summary_dto import OfficeOkrSummaryDto # noqa: PLC0415
        objectives: list[dict[str, Any]] | None | Unset
        if isinstance(self.objectives, Unset):
            objectives = UNSET
        elif isinstance(self.objectives, list):
            objectives = []
            for objectives_type_0_item_data in self.objectives:
                objectives_type_0_item = objectives_type_0_item_data.to_dict()
                objectives.append(objectives_type_0_item)


        else:
            objectives = self.objectives

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_objective_dto import OfficeObjectiveDto # noqa: PLC0415
        from ..models.office_okr_summary_dto import OfficeOkrSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_objectives(data: object) -> list[OfficeObjectiveDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                objectives_type_0 = []
                _objectives_type_0 = data
                for objectives_type_0_item_data in (_objectives_type_0):
                    objectives_type_0_item = OfficeObjectiveDto.from_dict(objectives_type_0_item_data)



                    objectives_type_0.append(objectives_type_0_item)

                return objectives_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeObjectiveDto] | None | Unset, data)

        objectives = _parse_objectives(d.pop("objectives", UNSET))


        _summary = d.pop("summary", UNSET)
        summary: OfficeOkrSummaryDto | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = OfficeOkrSummaryDto.from_dict(_summary)




        office_objective_list_dto = cls(
            objectives=objectives,
            summary=summary,
        )

        return office_objective_list_dto

