from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeDuplicateTableResult")



@_attrs_define
class OfficeDuplicateTableResult:
    

    records_copied: int | Unset = UNSET
    table_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        records_copied = self.records_copied

        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if records_copied is not UNSET:
            field_dict["recordsCopied"] = records_copied
        if table_id is not UNSET:
            field_dict["tableId"] = table_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        records_copied = d.pop("recordsCopied", UNSET)

        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id,  Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)




        office_duplicate_table_result = cls(
            records_copied=records_copied,
            table_id=table_id,
        )

        return office_duplicate_table_result

