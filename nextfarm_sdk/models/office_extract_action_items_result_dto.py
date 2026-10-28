from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeExtractActionItemsResultDto")



@_attrs_define
class OfficeExtractActionItemsResultDto:
    

    created_task_ids: list[UUID] | None | Unset = UNSET
    skipped_already_extracted: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_task_ids: list[str] | None | Unset
        if isinstance(self.created_task_ids, Unset):
            created_task_ids = UNSET
        elif isinstance(self.created_task_ids, list):
            created_task_ids = []
            for created_task_ids_type_0_item_data in self.created_task_ids:
                created_task_ids_type_0_item = str(created_task_ids_type_0_item_data)
                created_task_ids.append(created_task_ids_type_0_item)


        else:
            created_task_ids = self.created_task_ids

        skipped_already_extracted = self.skipped_already_extracted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_task_ids is not UNSET:
            field_dict["createdTaskIds"] = created_task_ids
        if skipped_already_extracted is not UNSET:
            field_dict["skippedAlreadyExtracted"] = skipped_already_extracted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_created_task_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                created_task_ids_type_0 = []
                _created_task_ids_type_0 = data
                for created_task_ids_type_0_item_data in (_created_task_ids_type_0):
                    created_task_ids_type_0_item = UUID(created_task_ids_type_0_item_data)



                    created_task_ids_type_0.append(created_task_ids_type_0_item)

                return created_task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        created_task_ids = _parse_created_task_ids(d.pop("createdTaskIds", UNSET))


        skipped_already_extracted = d.pop("skippedAlreadyExtracted", UNSET)

        office_extract_action_items_result_dto = cls(
            created_task_ids=created_task_ids,
            skipped_already_extracted=skipped_already_extracted,
        )

        return office_extract_action_items_result_dto

