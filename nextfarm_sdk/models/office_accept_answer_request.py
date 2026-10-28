from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeAcceptAnswerRequest")



@_attrs_define
class OfficeAcceptAnswerRequest:
    

    answer_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        answer_id: str | Unset = UNSET
        if not isinstance(self.answer_id, Unset):
            answer_id = str(self.answer_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if answer_id is not UNSET:
            field_dict["answerId"] = answer_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _answer_id = d.pop("answerId", UNSET)
        answer_id: UUID | Unset
        if isinstance(_answer_id,  Unset):
            answer_id = UNSET
        else:
            answer_id = UUID(_answer_id)




        office_accept_answer_request = cls(
            answer_id=answer_id,
        )

        return office_accept_answer_request

