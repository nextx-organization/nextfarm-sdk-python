from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAddReviewParticipantRequest")



@_attrs_define
class OfficeAddReviewParticipantRequest:
    

    employee_id: UUID | Unset = UNSET
    objective_id: None | Unset | UUID = UNSET
    reviewer_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        employee_id: str | Unset = UNSET
        if not isinstance(self.employee_id, Unset):
            employee_id = str(self.employee_id)

        objective_id: None | str | Unset
        if isinstance(self.objective_id, Unset):
            objective_id = UNSET
        elif isinstance(self.objective_id, UUID):
            objective_id = str(self.objective_id)
        else:
            objective_id = self.objective_id

        reviewer_id: None | str | Unset
        if isinstance(self.reviewer_id, Unset):
            reviewer_id = UNSET
        elif isinstance(self.reviewer_id, UUID):
            reviewer_id = str(self.reviewer_id)
        else:
            reviewer_id = self.reviewer_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if employee_id is not UNSET:
            field_dict["employeeId"] = employee_id
        if objective_id is not UNSET:
            field_dict["objectiveId"] = objective_id
        if reviewer_id is not UNSET:
            field_dict["reviewerId"] = reviewer_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _employee_id = d.pop("employeeId", UNSET)
        employee_id: UUID | Unset
        if isinstance(_employee_id,  Unset):
            employee_id = UNSET
        else:
            employee_id = UUID(_employee_id)




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


        def _parse_reviewer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewer_id_type_0 = UUID(data)



                return reviewer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reviewer_id = _parse_reviewer_id(d.pop("reviewerId", UNSET))


        office_add_review_participant_request = cls(
            employee_id=employee_id,
            objective_id=objective_id,
            reviewer_id=reviewer_id,
        )

        return office_add_review_participant_request

