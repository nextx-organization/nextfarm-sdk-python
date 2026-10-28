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
  from ..models.office_task_team_member_summary_dto import OfficeTaskTeamMemberSummaryDto





T = TypeVar("T", bound="OfficeTaskDepartmentSummaryDto")



@_attrs_define
class OfficeTaskDepartmentSummaryDto:
    

    counts: OfficeTaskSummaryCountsDto | Unset = UNSET
    direct_counts: OfficeTaskSummaryCountsDto | Unset = UNSET
    direct_member_ids: list[UUID] | None | Unset = UNSET
    head_user_id: None | Unset | UUID = UNSET
    id: UUID | Unset = UNSET
    member_ids: list[UUID] | None | Unset = UNSET
    members: list[OfficeTaskTeamMemberSummaryDto] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        from ..models.office_task_team_member_summary_dto import OfficeTaskTeamMemberSummaryDto # noqa: PLC0415
        counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        direct_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direct_counts, Unset):
            direct_counts = self.direct_counts.to_dict()

        direct_member_ids: list[str] | None | Unset
        if isinstance(self.direct_member_ids, Unset):
            direct_member_ids = UNSET
        elif isinstance(self.direct_member_ids, list):
            direct_member_ids = []
            for direct_member_ids_type_0_item_data in self.direct_member_ids:
                direct_member_ids_type_0_item = str(direct_member_ids_type_0_item_data)
                direct_member_ids.append(direct_member_ids_type_0_item)


        else:
            direct_member_ids = self.direct_member_ids

        head_user_id: None | str | Unset
        if isinstance(self.head_user_id, Unset):
            head_user_id = UNSET
        elif isinstance(self.head_user_id, UUID):
            head_user_id = str(self.head_user_id)
        else:
            head_user_id = self.head_user_id

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if counts is not UNSET:
            field_dict["counts"] = counts
        if direct_counts is not UNSET:
            field_dict["directCounts"] = direct_counts
        if direct_member_ids is not UNSET:
            field_dict["directMemberIds"] = direct_member_ids
        if head_user_id is not UNSET:
            field_dict["headUserId"] = head_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if member_ids is not UNSET:
            field_dict["memberIds"] = member_ids
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_summary_counts_dto import OfficeTaskSummaryCountsDto # noqa: PLC0415
        from ..models.office_task_team_member_summary_dto import OfficeTaskTeamMemberSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        _counts = d.pop("counts", UNSET)
        counts: OfficeTaskSummaryCountsDto | Unset
        if isinstance(_counts,  Unset):
            counts = UNSET
        else:
            counts = OfficeTaskSummaryCountsDto.from_dict(_counts)




        _direct_counts = d.pop("directCounts", UNSET)
        direct_counts: OfficeTaskSummaryCountsDto | Unset
        if isinstance(_direct_counts,  Unset):
            direct_counts = UNSET
        else:
            direct_counts = OfficeTaskSummaryCountsDto.from_dict(_direct_counts)




        def _parse_direct_member_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                direct_member_ids_type_0 = []
                _direct_member_ids_type_0 = data
                for direct_member_ids_type_0_item_data in (_direct_member_ids_type_0):
                    direct_member_ids_type_0_item = UUID(direct_member_ids_type_0_item_data)



                    direct_member_ids_type_0.append(direct_member_ids_type_0_item)

                return direct_member_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        direct_member_ids = _parse_direct_member_ids(d.pop("directMemberIds", UNSET))


        def _parse_head_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                head_user_id_type_0 = UUID(data)



                return head_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        head_user_id = _parse_head_user_id(d.pop("headUserId", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)



                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        office_task_department_summary_dto = cls(
            counts=counts,
            direct_counts=direct_counts,
            direct_member_ids=direct_member_ids,
            head_user_id=head_user_id,
            id=id,
            member_ids=member_ids,
            members=members,
            name=name,
            parent_id=parent_id,
        )

        return office_task_department_summary_dto

