from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HarvestCollectHarvestRequest")



@_attrs_define
class HarvestCollectHarvestRequest:
    

    collection_notes: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        collection_notes: None | str | Unset
        if isinstance(self.collection_notes, Unset):
            collection_notes = UNSET
        else:
            collection_notes = self.collection_notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if collection_notes is not UNSET:
            field_dict["collection_notes"] = collection_notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_collection_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_notes = _parse_collection_notes(d.pop("collection_notes", UNSET))


        harvest_collect_harvest_request = cls(
            collection_notes=collection_notes,
        )

        return harvest_collect_harvest_request

