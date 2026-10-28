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
  from ..models.office_review_form_item_dto import OfficeReviewFormItemDto





T = TypeVar("T", bound="OfficeReviewFormDto")



@_attrs_define
class OfficeReviewFormDto:
    

    can_edit_manager: bool | Unset = UNSET
    can_edit_self: bool | Unset = UNSET
    cycle_id: UUID | Unset = UNSET
    cycle_name: None | str | Unset = UNSET
    cycle_status: None | str | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    employee_id: UUID | Unset = UNSET
    finalized_at: datetime.datetime | None | Unset = UNSET
    id: UUID | Unset = UNSET
    items: list[OfficeReviewFormItemDto] | None | Unset = UNSET
    manager_feedback_visible: bool | Unset = UNSET
    manager_overall_score: float | None | Unset = UNSET
    manager_summary: None | str | Unset = UNSET
    objective_id: None | Unset | UUID = UNSET
    reviewer_id: UUID | Unset = UNSET
    self_overall_score: float | None | Unset = UNSET
    self_submitted_at: datetime.datetime | None | Unset = UNSET
    self_summary: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    viewer_role: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_review_form_item_dto import OfficeReviewFormItemDto # noqa: PLC0415
        can_edit_manager = self.can_edit_manager

        can_edit_self = self.can_edit_self

        cycle_id: str | Unset = UNSET
        if not isinstance(self.cycle_id, Unset):
            cycle_id = str(self.cycle_id)

        cycle_name: None | str | Unset
        if isinstance(self.cycle_name, Unset):
            cycle_name = UNSET
        else:
            cycle_name = self.cycle_name

        cycle_status: None | str | Unset
        if isinstance(self.cycle_status, Unset):
            cycle_status = UNSET
        else:
            cycle_status = self.cycle_status

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        finalized_at: None | str | Unset
        if isinstance(self.finalized_at, Unset):
            finalized_at = UNSET
        elif isinstance(self.finalized_at, datetime.datetime):
            finalized_at = self.finalized_at.isoformat()
        else:
            finalized_at = self.finalized_at

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        manager_feedback_visible = self.manager_feedback_visible

        manager_overall_score: float | None | Unset
        if isinstance(self.manager_overall_score, Unset):
            manager_overall_score = UNSET
        else:
            manager_overall_score = self.manager_overall_score

        manager_summary: None | str | Unset
        if isinstance(self.manager_summary, Unset):
            manager_summary = UNSET
        else:
            manager_summary = self.manager_summary

        objective_id: None | str | Unset
        if isinstance(self.objective_id, Unset):
            objective_id = UNSET
        elif isinstance(self.objective_id, UUID):
            objective_id = str(self.objective_id)
        else:
            objective_id = self.objective_id

        reviewer_id: str | Unset = UNSET
        if not isinstance(self.reviewer_id, Unset):
            reviewer_id = str(self.reviewer_id)

        self_overall_score: float | None | Unset
        if isinstance(self.self_overall_score, Unset):
            self_overall_score = UNSET
        else:
            self_overall_score = self.self_overall_score

        self_submitted_at: None | str | Unset
        if isinstance(self.self_submitted_at, Unset):
            self_submitted_at = UNSET
        elif isinstance(self.self_submitted_at, datetime.datetime):
            self_submitted_at = self.self_submitted_at.isoformat()
        else:
            self_submitted_at = self.self_submitted_at

        self_summary: None | str | Unset
        if isinstance(self.self_summary, Unset):
            self_summary = UNSET
        else:
            self_summary = self.self_summary

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        viewer_role: None | str | Unset
        if isinstance(self.viewer_role, Unset):
            viewer_role = UNSET
        else:
            viewer_role = self.viewer_role


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_edit_manager is not UNSET:
            field_dict["canEditManager"] = can_edit_manager
        if can_edit_self is not UNSET:
            field_dict["canEditSelf"] = can_edit_self
        if cycle_id is not UNSET:
            field_dict["cycleId"] = cycle_id
        if cycle_name is not UNSET:
            field_dict["cycleName"] = cycle_name
        if cycle_status is not UNSET:
            field_dict["cycleStatus"] = cycle_status
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if finalized_at is not UNSET:
            field_dict["finalizedAt"] = finalized_at
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items
        if manager_feedback_visible is not UNSET:
            field_dict["managerFeedbackVisible"] = manager_feedback_visible
        if manager_overall_score is not UNSET:
            field_dict["managerOverallScore"] = manager_overall_score
        if manager_summary is not UNSET:
            field_dict["managerSummary"] = manager_summary
        if objective_id is not UNSET:
            field_dict["objectiveId"] = objective_id
        if reviewer_id is not UNSET:
            field_dict["reviewerId"] = reviewer_id
        if self_overall_score is not UNSET:
            field_dict["selfOverallScore"] = self_overall_score
        if self_submitted_at is not UNSET:
            field_dict["selfSubmittedAt"] = self_submitted_at
        if self_summary is not UNSET:
            field_dict["selfSummary"] = self_summary
        if status is not UNSET:
            field_dict["status"] = status
        if viewer_role is not UNSET:
            field_dict["viewerRole"] = viewer_role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_review_form_item_dto import OfficeReviewFormItemDto # noqa: PLC0415
        d = dict(src_dict)
        can_edit_manager = d.pop("canEditManager", UNSET)

        can_edit_self = d.pop("canEditSelf", UNSET)

        _cycle_id = d.pop("cycleId", UNSET)
        cycle_id: UUID | Unset
        if isinstance(_cycle_id,  Unset):
            cycle_id = UNSET
        else:
            cycle_id = UUID(_cycle_id)




        def _parse_cycle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cycle_name = _parse_cycle_name(d.pop("cycleName", UNSET))


        def _parse_cycle_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cycle_status = _parse_cycle_status(d.pop("cycleStatus", UNSET))


        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date,  Unset):
            due_date = UNSET
        else:
            due_date = datetime.datetime.fromisoformat(_due_date)




        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




        def _parse_finalized_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finalized_at_type_0 = datetime.datetime.fromisoformat(data)



                return finalized_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finalized_at = _parse_finalized_at(d.pop("finalizedAt", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        def _parse_items(data: object) -> list[OfficeReviewFormItemDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = OfficeReviewFormItemDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeReviewFormItemDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        manager_feedback_visible = d.pop("managerFeedbackVisible", UNSET)

        def _parse_manager_overall_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        manager_overall_score = _parse_manager_overall_score(d.pop("managerOverallScore", UNSET))


        def _parse_manager_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manager_summary = _parse_manager_summary(d.pop("managerSummary", UNSET))


        def _parse_objective_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                objective_id_type_0 = UUID(data)



                return objective_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        objective_id = _parse_objective_id(d.pop("objectiveId", UNSET))


        _reviewer_id = d.pop("reviewerId", UNSET)
        reviewer_id: UUID | Unset
        if isinstance(_reviewer_id,  Unset):
            reviewer_id = UNSET
        else:
            reviewer_id = UUID(_reviewer_id)




        def _parse_self_overall_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        self_overall_score = _parse_self_overall_score(d.pop("selfOverallScore", UNSET))


        def _parse_self_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                self_submitted_at_type_0 = datetime.datetime.fromisoformat(data)



                return self_submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        self_submitted_at = _parse_self_submitted_at(d.pop("selfSubmittedAt", UNSET))


        def _parse_self_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        self_summary = _parse_self_summary(d.pop("selfSummary", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_viewer_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        viewer_role = _parse_viewer_role(d.pop("viewerRole", UNSET))


        office_review_form_dto = cls(
            can_edit_manager=can_edit_manager,
            can_edit_self=can_edit_self,
            cycle_id=cycle_id,
            cycle_name=cycle_name,
            cycle_status=cycle_status,
            due_date=due_date,
            employee_id=employee_id,
            finalized_at=finalized_at,
            id=id,
            items=items,
            manager_feedback_visible=manager_feedback_visible,
            manager_overall_score=manager_overall_score,
            manager_summary=manager_summary,
            objective_id=objective_id,
            reviewer_id=reviewer_id,
            self_overall_score=self_overall_score,
            self_submitted_at=self_submitted_at,
            self_summary=self_summary,
            status=status,
            viewer_role=viewer_role,
        )

        return office_review_form_dto

