from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_find_replace_change import OfficeFindReplaceChange





T = TypeVar("T", bound="OfficeFindReplaceResult")



@_attrs_define
class OfficeFindReplaceResult:
    

    applied: bool | Unset = UNSET
    changes: list[OfficeFindReplaceChange] | None | Unset = UNSET
    matched_cells: int | Unset = UNSET
    matched_records: int | Unset = UNSET
    truncated: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_find_replace_change import OfficeFindReplaceChange # noqa: PLC0415
        applied = self.applied

        changes: list[dict[str, Any]] | None | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.to_dict()
                changes.append(changes_type_0_item)


        else:
            changes = self.changes

        matched_cells = self.matched_cells

        matched_records = self.matched_records

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if applied is not UNSET:
            field_dict["applied"] = applied
        if changes is not UNSET:
            field_dict["changes"] = changes
        if matched_cells is not UNSET:
            field_dict["matchedCells"] = matched_cells
        if matched_records is not UNSET:
            field_dict["matchedRecords"] = matched_records
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_find_replace_change import OfficeFindReplaceChange # noqa: PLC0415
        d = dict(src_dict)
        applied = d.pop("applied", UNSET)

        def _parse_changes(data: object) -> list[OfficeFindReplaceChange] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in (_changes_type_0):
                    changes_type_0_item = OfficeFindReplaceChange.from_dict(changes_type_0_item_data)



                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeFindReplaceChange] | None | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))


        matched_cells = d.pop("matchedCells", UNSET)

        matched_records = d.pop("matchedRecords", UNSET)

        truncated = d.pop("truncated", UNSET)

        office_find_replace_result = cls(
            applied=applied,
            changes=changes,
            matched_cells=matched_cells,
            matched_records=matched_records,
            truncated=truncated,
        )

        return office_find_replace_result

