from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_review_criterion_input import OfficeReviewCriterionInput





T = TypeVar("T", bound="OfficeReplaceReviewCriteriaRequest")



@_attrs_define
class OfficeReplaceReviewCriteriaRequest:
    

    criteria: list[OfficeReviewCriterionInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_review_criterion_input import OfficeReviewCriterionInput # noqa: PLC0415
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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if criteria is not UNSET:
            field_dict["criteria"] = criteria

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_review_criterion_input import OfficeReviewCriterionInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_criteria(data: object) -> list[OfficeReviewCriterionInput] | None | Unset:
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
                    criteria_type_0_item = OfficeReviewCriterionInput.from_dict(criteria_type_0_item_data)



                    criteria_type_0.append(criteria_type_0_item)

                return criteria_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeReviewCriterionInput] | None | Unset, data)

        criteria = _parse_criteria(d.pop("criteria", UNSET))


        office_replace_review_criteria_request = cls(
            criteria=criteria,
        )

        return office_replace_review_criteria_request

