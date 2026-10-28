from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeReviewFormItemDto")



@_attrs_define
class OfficeReviewFormItemDto:
    

    criterion_description: None | str | Unset = UNSET
    criterion_id: UUID | Unset = UNSET
    criterion_name: None | str | Unset = UNSET
    manager_comment: None | str | Unset = UNSET
    manager_score: int | None | Unset = UNSET
    self_comment: None | str | Unset = UNSET
    self_score: int | None | Unset = UNSET
    sort_order: int | Unset = UNSET
    weight_percent: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        criterion_description: None | str | Unset
        if isinstance(self.criterion_description, Unset):
            criterion_description = UNSET
        else:
            criterion_description = self.criterion_description

        criterion_id: str | Unset = UNSET
        if not isinstance(self.criterion_id, Unset):
            criterion_id = str(self.criterion_id)

        criterion_name: None | str | Unset
        if isinstance(self.criterion_name, Unset):
            criterion_name = UNSET
        else:
            criterion_name = self.criterion_name

        manager_comment: None | str | Unset
        if isinstance(self.manager_comment, Unset):
            manager_comment = UNSET
        else:
            manager_comment = self.manager_comment

        manager_score: int | None | Unset
        if isinstance(self.manager_score, Unset):
            manager_score = UNSET
        else:
            manager_score = self.manager_score

        self_comment: None | str | Unset
        if isinstance(self.self_comment, Unset):
            self_comment = UNSET
        else:
            self_comment = self.self_comment

        self_score: int | None | Unset
        if isinstance(self.self_score, Unset):
            self_score = UNSET
        else:
            self_score = self.self_score

        sort_order = self.sort_order

        weight_percent = self.weight_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if criterion_description is not UNSET:
            field_dict["criterionDescription"] = criterion_description
        if criterion_id is not UNSET:
            field_dict["criterionId"] = criterion_id
        if criterion_name is not UNSET:
            field_dict["criterionName"] = criterion_name
        if manager_comment is not UNSET:
            field_dict["managerComment"] = manager_comment
        if manager_score is not UNSET:
            field_dict["managerScore"] = manager_score
        if self_comment is not UNSET:
            field_dict["selfComment"] = self_comment
        if self_score is not UNSET:
            field_dict["selfScore"] = self_score
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if weight_percent is not UNSET:
            field_dict["weightPercent"] = weight_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_criterion_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        criterion_description = _parse_criterion_description(d.pop("criterionDescription", UNSET))


        _criterion_id = d.pop("criterionId", UNSET)
        criterion_id: UUID | Unset
        if isinstance(_criterion_id,  Unset):
            criterion_id = UNSET
        else:
            criterion_id = UUID(_criterion_id)




        def _parse_criterion_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        criterion_name = _parse_criterion_name(d.pop("criterionName", UNSET))


        def _parse_manager_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manager_comment = _parse_manager_comment(d.pop("managerComment", UNSET))


        def _parse_manager_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        manager_score = _parse_manager_score(d.pop("managerScore", UNSET))


        def _parse_self_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        self_comment = _parse_self_comment(d.pop("selfComment", UNSET))


        def _parse_self_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        self_score = _parse_self_score(d.pop("selfScore", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        weight_percent = d.pop("weightPercent", UNSET)

        office_review_form_item_dto = cls(
            criterion_description=criterion_description,
            criterion_id=criterion_id,
            criterion_name=criterion_name,
            manager_comment=manager_comment,
            manager_score=manager_score,
            self_comment=self_comment,
            self_score=self_score,
            sort_order=sort_order,
            weight_percent=weight_percent,
        )

        return office_review_form_item_dto

