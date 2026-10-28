from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_review_form_dto import OfficeReviewFormDto
  from ..models.office_review_form_summary_dto import OfficeReviewFormSummaryDto





T = TypeVar("T", bound="OfficeReviewFormListDto")



@_attrs_define
class OfficeReviewFormListDto:
    

    forms: list[OfficeReviewFormDto] | None | Unset = UNSET
    summary: OfficeReviewFormSummaryDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_review_form_dto import OfficeReviewFormDto # noqa: PLC0415
        from ..models.office_review_form_summary_dto import OfficeReviewFormSummaryDto # noqa: PLC0415
        forms: list[dict[str, Any]] | None | Unset
        if isinstance(self.forms, Unset):
            forms = UNSET
        elif isinstance(self.forms, list):
            forms = []
            for forms_type_0_item_data in self.forms:
                forms_type_0_item = forms_type_0_item_data.to_dict()
                forms.append(forms_type_0_item)


        else:
            forms = self.forms

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if forms is not UNSET:
            field_dict["forms"] = forms
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_review_form_dto import OfficeReviewFormDto # noqa: PLC0415
        from ..models.office_review_form_summary_dto import OfficeReviewFormSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_forms(data: object) -> list[OfficeReviewFormDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                forms_type_0 = []
                _forms_type_0 = data
                for forms_type_0_item_data in (_forms_type_0):
                    forms_type_0_item = OfficeReviewFormDto.from_dict(forms_type_0_item_data)



                    forms_type_0.append(forms_type_0_item)

                return forms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeReviewFormDto] | None | Unset, data)

        forms = _parse_forms(d.pop("forms", UNSET))


        _summary = d.pop("summary", UNSET)
        summary: OfficeReviewFormSummaryDto | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = OfficeReviewFormSummaryDto.from_dict(_summary)




        office_review_form_list_dto = cls(
            forms=forms,
            summary=summary,
        )

        return office_review_form_list_dto

