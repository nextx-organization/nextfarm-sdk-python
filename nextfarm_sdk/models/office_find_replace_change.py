from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeFindReplaceChange")



@_attrs_define
class OfficeFindReplaceChange:
    

    after: None | str | Unset = UNSET
    before: None | str | Unset = UNSET
    field_id: UUID | Unset = UNSET
    record_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        after: None | str | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        else:
            after = self.after

        before: None | str | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        else:
            before = self.before

        field_id: str | Unset = UNSET
        if not isinstance(self.field_id, Unset):
            field_id = str(self.field_id)

        record_id: str | Unset = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = str(self.record_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if field_id is not UNSET:
            field_dict["fieldId"] = field_id
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after = _parse_after(d.pop("after", UNSET))


        def _parse_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        before = _parse_before(d.pop("before", UNSET))


        _field_id = d.pop("fieldId", UNSET)
        field_id: UUID | Unset
        if isinstance(_field_id,  Unset):
            field_id = UNSET
        else:
            field_id = UUID(_field_id)




        _record_id = d.pop("recordId", UNSET)
        record_id: UUID | Unset
        if isinstance(_record_id,  Unset):
            record_id = UNSET
        else:
            record_id = UUID(_record_id)




        office_find_replace_change = cls(
            after=after,
            before=before,
            field_id=field_id,
            record_id=record_id,
        )

        return office_find_replace_change

