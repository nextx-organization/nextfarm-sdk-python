from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_automation_summary_dto_by_trigger_type_0 import OfficeAutomationSummaryDtoByTriggerType0





T = TypeVar("T", bound="OfficeAutomationSummaryDto")



@_attrs_define
class OfficeAutomationSummaryDto:
    

    active: int | Unset = UNSET
    archived: int | Unset = UNSET
    by_trigger: None | OfficeAutomationSummaryDtoByTriggerType0 | Unset = UNSET
    failing: int | Unset = UNSET
    inactive: int | Unset = UNSET
    mine: int | Unset = UNSET
    total: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_automation_summary_dto_by_trigger_type_0 import OfficeAutomationSummaryDtoByTriggerType0 # noqa: PLC0415
        active = self.active

        archived = self.archived

        by_trigger: dict[str, Any] | None | Unset
        if isinstance(self.by_trigger, Unset):
            by_trigger = UNSET
        elif isinstance(self.by_trigger, OfficeAutomationSummaryDtoByTriggerType0):
            by_trigger = self.by_trigger.to_dict()
        else:
            by_trigger = self.by_trigger

        failing = self.failing

        inactive = self.inactive

        mine = self.mine

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if archived is not UNSET:
            field_dict["archived"] = archived
        if by_trigger is not UNSET:
            field_dict["byTrigger"] = by_trigger
        if failing is not UNSET:
            field_dict["failing"] = failing
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if mine is not UNSET:
            field_dict["mine"] = mine
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_automation_summary_dto_by_trigger_type_0 import OfficeAutomationSummaryDtoByTriggerType0 # noqa: PLC0415
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        archived = d.pop("archived", UNSET)

        def _parse_by_trigger(data: object) -> None | OfficeAutomationSummaryDtoByTriggerType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                by_trigger_type_0 = OfficeAutomationSummaryDtoByTriggerType0.from_dict(data)



                return by_trigger_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeAutomationSummaryDtoByTriggerType0 | Unset, data)

        by_trigger = _parse_by_trigger(d.pop("byTrigger", UNSET))


        failing = d.pop("failing", UNSET)

        inactive = d.pop("inactive", UNSET)

        mine = d.pop("mine", UNSET)

        total = d.pop("total", UNSET)

        office_automation_summary_dto = cls(
            active=active,
            archived=archived,
            by_trigger=by_trigger,
            failing=failing,
            inactive=inactive,
            mine=mine,
            total=total,
        )

        return office_automation_summary_dto

