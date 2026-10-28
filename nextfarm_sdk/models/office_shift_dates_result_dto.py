from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OfficeShiftDatesResultDto")



@_attrs_define
class OfficeShiftDatesResultDto:
    

    kept_done: int | Unset = UNSET
    kept_undated: int | Unset = UNSET
    shifted: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        kept_done = self.kept_done

        kept_undated = self.kept_undated

        shifted = self.shifted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if kept_done is not UNSET:
            field_dict["keptDone"] = kept_done
        if kept_undated is not UNSET:
            field_dict["keptUndated"] = kept_undated
        if shifted is not UNSET:
            field_dict["shifted"] = shifted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kept_done = d.pop("keptDone", UNSET)

        kept_undated = d.pop("keptUndated", UNSET)

        shifted = d.pop("shifted", UNSET)

        office_shift_dates_result_dto = cls(
            kept_done=kept_done,
            kept_undated=kept_undated,
            shifted=shifted,
        )

        return office_shift_dates_result_dto

