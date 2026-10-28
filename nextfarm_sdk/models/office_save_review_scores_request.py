from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_review_score_input import OfficeReviewScoreInput





T = TypeVar("T", bound="OfficeSaveReviewScoresRequest")



@_attrs_define
class OfficeSaveReviewScoresRequest:
    

    scores: list[OfficeReviewScoreInput] | None | Unset = UNSET
    summary: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_review_score_input import OfficeReviewScoreInput # noqa: PLC0415
        scores: list[dict[str, Any]] | None | Unset
        if isinstance(self.scores, Unset):
            scores = UNSET
        elif isinstance(self.scores, list):
            scores = []
            for scores_type_0_item_data in self.scores:
                scores_type_0_item = scores_type_0_item_data.to_dict()
                scores.append(scores_type_0_item)


        else:
            scores = self.scores

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if scores is not UNSET:
            field_dict["scores"] = scores
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_review_score_input import OfficeReviewScoreInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_scores(data: object) -> list[OfficeReviewScoreInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scores_type_0 = []
                _scores_type_0 = data
                for scores_type_0_item_data in (_scores_type_0):
                    scores_type_0_item = OfficeReviewScoreInput.from_dict(scores_type_0_item_data)



                    scores_type_0.append(scores_type_0_item)

                return scores_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeReviewScoreInput] | None | Unset, data)

        scores = _parse_scores(d.pop("scores", UNSET))


        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        office_save_review_scores_request = cls(
            scores=scores,
            summary=summary,
        )

        return office_save_review_scores_request

