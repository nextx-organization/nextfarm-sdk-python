from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeSetTaskListGroupTeamRequest")



@_attrs_define
class OfficeSetTaskListGroupTeamRequest:
    

    is_team: bool | Unset = UNSET
    lead_user_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_team = self.is_team

        lead_user_id: None | str | Unset
        if isinstance(self.lead_user_id, Unset):
            lead_user_id = UNSET
        elif isinstance(self.lead_user_id, UUID):
            lead_user_id = str(self.lead_user_id)
        else:
            lead_user_id = self.lead_user_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_team is not UNSET:
            field_dict["isTeam"] = is_team
        if lead_user_id is not UNSET:
            field_dict["leadUserId"] = lead_user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_team = d.pop("isTeam", UNSET)

        def _parse_lead_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lead_user_id_type_0 = UUID(data)



                return lead_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        lead_user_id = _parse_lead_user_id(d.pop("leadUserId", UNSET))


        office_set_task_list_group_team_request = cls(
            is_team=is_team,
            lead_user_id=lead_user_id,
        )

        return office_set_task_list_group_team_request

