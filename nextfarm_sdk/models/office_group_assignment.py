from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeGroupAssignment")



@_attrs_define
class OfficeGroupAssignment:
    

    assignee_id: UUID | Unset = UNSET
    group_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        assignee_id: str | Unset = UNSET
        if not isinstance(self.assignee_id, Unset):
            assignee_id = str(self.assignee_id)

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _assignee_id = d.pop("assigneeId", UNSET)
        assignee_id: UUID | Unset
        if isinstance(_assignee_id,  Unset):
            assignee_id = UNSET
        else:
            assignee_id = UUID(_assignee_id)




        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)



                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))


        office_group_assignment = cls(
            assignee_id=assignee_id,
            group_id=group_id,
        )

        return office_group_assignment

