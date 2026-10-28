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

if TYPE_CHECKING:
  from ..models.office_review_criterion_dto import OfficeReviewCriterionDto





T = TypeVar("T", bound="OfficeReviewCycleDto")



@_attrs_define
class OfficeReviewCycleDto:
    

    activated_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    criteria: list[OfficeReviewCriterionDto] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    form_count: int | Unset = UNSET
    id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    period_end: datetime.datetime | Unset = UNSET
    period_start: datetime.datetime | Unset = UNSET
    status: None | str | Unset = UNSET
    total_weight_percent: float | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_review_criterion_dto import OfficeReviewCriterionDto # noqa: PLC0415
        activated_at: None | str | Unset
        if isinstance(self.activated_at, Unset):
            activated_at = UNSET
        elif isinstance(self.activated_at, datetime.datetime):
            activated_at = self.activated_at.isoformat()
        else:
            activated_at = self.activated_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        criteria: list[dict[str, Any]] | None | Unset
        if isinstance(self.criteria, Unset):
            criteria = UNSET
        elif isinstance(self.criteria, list):
            criteria = []
            for criteria_type_0_item_data in self.criteria:
                criteria_type_0_item = criteria_type_0_item_data.to_dict()
                criteria.append(criteria_type_0_item)


        else:
            criteria = self.criteria

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        form_count = self.form_count

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        period_end: str | Unset = UNSET
        if not isinstance(self.period_end, Unset):
            period_end = self.period_end.isoformat()

        period_start: str | Unset = UNSET
        if not isinstance(self.period_start, Unset):
            period_start = self.period_start.isoformat()

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        total_weight_percent = self.total_weight_percent

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if activated_at is not UNSET:
            field_dict["activatedAt"] = activated_at
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if form_count is not UNSET:
            field_dict["formCount"] = form_count
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start
        if status is not UNSET:
            field_dict["status"] = status
        if total_weight_percent is not UNSET:
            field_dict["totalWeightPercent"] = total_weight_percent
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_review_criterion_dto import OfficeReviewCriterionDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_activated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activated_at_type_0 = datetime.datetime.fromisoformat(data)



                return activated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        activated_at = _parse_activated_at(d.pop("activatedAt", UNSET))


        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)



                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closedAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_criteria(data: object) -> list[OfficeReviewCriterionDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                criteria_type_0 = []
                _criteria_type_0 = data
                for criteria_type_0_item_data in (_criteria_type_0):
                    criteria_type_0_item = OfficeReviewCriterionDto.from_dict(criteria_type_0_item_data)



                    criteria_type_0.append(criteria_type_0_item)

                return criteria_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeReviewCriterionDto] | None | Unset, data)

        criteria = _parse_criteria(d.pop("criteria", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date,  Unset):
            due_date = UNSET
        else:
            due_date = datetime.datetime.fromisoformat(_due_date)




        form_count = d.pop("formCount", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _period_end = d.pop("periodEnd", UNSET)
        period_end: datetime.datetime | Unset
        if isinstance(_period_end,  Unset):
            period_end = UNSET
        else:
            period_end = datetime.datetime.fromisoformat(_period_end)




        _period_start = d.pop("periodStart", UNSET)
        period_start: datetime.datetime | Unset
        if isinstance(_period_start,  Unset):
            period_start = UNSET
        else:
            period_start = datetime.datetime.fromisoformat(_period_start)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        total_weight_percent = d.pop("totalWeightPercent", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_review_cycle_dto = cls(
            activated_at=activated_at,
            closed_at=closed_at,
            created_at=created_at,
            criteria=criteria,
            description=description,
            due_date=due_date,
            form_count=form_count,
            id=id,
            name=name,
            period_end=period_end,
            period_start=period_start,
            status=status,
            total_weight_percent=total_weight_percent,
            updated_at=updated_at,
        )

        return office_review_cycle_dto

