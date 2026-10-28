from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto
  from ..models.office_task_team_current_group_dto import OfficeTaskTeamCurrentGroupDto
  from ..models.office_task_team_current_list_dto import OfficeTaskTeamCurrentListDto
  from ..models.office_task_team_member_summary_dto import OfficeTaskTeamMemberSummaryDto





T = TypeVar("T", bound="OfficeTaskTeamSummaryDto")



@_attrs_define
class OfficeTaskTeamSummaryDto:
    

    counts: OfficeTaskSummaryCountsDto | Unset = UNSET
    current_group: OfficeTaskTeamCurrentGroupDto | Unset = UNSET
    current_list: OfficeTaskTeamCurrentListDto | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    lead_user_id: None | Unset | UUID = UNSET
    member_ids: list[UUID] | None | Unset = UNSET
    members: list[OfficeTaskTeamMemberSummaryDto] | None | Unset = UNSET
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        from ..models.office_task_team_current_group_dto import OfficeTaskTeamCurrentGroupDto # noqa: PLC0415
        from ..models.office_task_team_current_list_dto import OfficeTaskTeamCurrentListDto # noqa: PLC0415
        from ..models.office_task_team_member_summary_dto import OfficeTaskTeamMemberSummaryDto # noqa: PLC0415
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        current_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_group, Unset):
            current_group = self.current_group.to_dict()

        current_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_list, Unset):
            current_list = self.current_list.to_dict()

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        lead_user_id: None | str | Unset
        if isinstance(self.lead_user_id, Unset):
            lead_user_id = UNSET
        elif isinstance(self.lead_user_id, UUID):
            lead_user_id = str(self.lead_user_id)
        else:
            lead_user_id = self.lead_user_id

        member_ids: list[str] | None | Unset
        if isinstance(self.member_ids, Unset):
            member_ids = UNSET
        elif isinstance(self.member_ids, list):
            member_ids = []
            for member_ids_type_0_item_data in self.member_ids:
                member_ids_type_0_item = str(member_ids_type_0_item_data)
                member_ids.append(member_ids_type_0_item)


        else:
            member_ids = self.member_ids

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if counts is not UNSET:
            field_dict["counts"] = counts
        if current_group is not UNSET:
            field_dict["currentGroup"] = current_group
        if current_list is not UNSET:
            field_dict["currentList"] = current_list
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if id is not UNSET:
            field_dict["id"] = id
        if lead_user_id is not UNSET:
            field_dict["leadUserId"] = lead_user_id
        if member_ids is not UNSET:
            field_dict["memberIds"] = member_ids
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        from ..models.office_task_team_current_group_dto import OfficeTaskTeamCurrentGroupDto # noqa: PLC0415
        from ..models.office_task_team_current_list_dto import OfficeTaskTeamCurrentListDto # noqa: PLC0415
        from ..models.office_task_team_member_summary_dto import OfficeTaskTeamMemberSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: OfficeTaskSummaryCountsDto | Unset
        if isinstance(_counts,  Unset):
            counts = UNSET
        else:
            counts = OfficeTaskSummaryCountsDto.from_dict(_counts)




        _current_group = d.pop("currentGroup", UNSET)
        current_group: OfficeTaskTeamCurrentGroupDto | Unset
        if isinstance(_current_group,  Unset):
            current_group = UNSET
        else:
            current_group = OfficeTaskTeamCurrentGroupDto.from_dict(_current_group)




        _current_list = d.pop("currentList", UNSET)
        current_list: OfficeTaskTeamCurrentListDto | Unset
        if isinstance(_current_list,  Unset):
            current_list = UNSET
        else:
            current_list = OfficeTaskTeamCurrentListDto.from_dict(_current_list)




        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)



                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("departmentId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        def _parse_member_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_ids_type_0 = []
                _member_ids_type_0 = data
                for member_ids_type_0_item_data in (_member_ids_type_0):
                    member_ids_type_0_item = UUID(member_ids_type_0_item_data)



                    member_ids_type_0.append(member_ids_type_0_item)

                return member_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        member_ids = _parse_member_ids(d.pop("memberIds", UNSET))


        def _parse_members(data: object) -> list[OfficeTaskTeamMemberSummaryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = OfficeTaskTeamMemberSummaryDto.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskTeamMemberSummaryDto] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        office_task_team_summary_dto = cls(
            counts=counts,
            current_group=current_group,
            current_list=current_list,
            department_id=department_id,
            id=id,
            lead_user_id=lead_user_id,
            member_ids=member_ids,
            members=members,
            name=name,
        )

        return office_task_team_summary_dto

