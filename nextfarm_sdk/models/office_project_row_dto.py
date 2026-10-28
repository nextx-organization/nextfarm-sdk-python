from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_project_health_reason_dto import OfficeProjectHealthReasonDto





T = TypeVar("T", bound="OfficeProjectRowDto")



@_attrs_define
class OfficeProjectRowDto:
    

    active: int | Unset = UNSET
    color_tag: None | str | Unset = UNSET
    done: int | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    folder_id: None | Unset | UUID = UNSET
    health: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_pinned: bool | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    lead_user_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    open_: int | Unset = UNSET
    overdue: int | Unset = UNSET
    owner_id: UUID | Unset = UNSET
    reasons: list[OfficeProjectHealthReasonDto] | None | Unset = UNSET
    stage_count: int | Unset = UNSET
    stage_index: int | None | Unset = UNSET
    stage_name: None | str | Unset = UNSET
    total: int | Unset = UNSET
    unassigned: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_project_health_reason_dto import OfficeProjectHealthReasonDto # noqa: PLC0415
        active = self.active

        color_tag: None | str | Unset
        if isinstance(self.color_tag, Unset):
            color_tag = UNSET
        else:
            color_tag = self.color_tag

        done = self.done

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        folder_id: None | str | Unset
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        elif isinstance(self.folder_id, UUID):
            folder_id = str(self.folder_id)
        else:
            folder_id = self.folder_id

        health: None | str | Unset
        if isinstance(self.health, Unset):
            health = UNSET
        else:
            health = self.health

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_archived = self.is_archived

        is_pinned = self.is_pinned

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        lead_user_id: None | str | Unset
        if isinstance(self.lead_user_id, Unset):
            lead_user_id = UNSET
        elif isinstance(self.lead_user_id, UUID):
            lead_user_id = str(self.lead_user_id)
        else:
            lead_user_id = self.lead_user_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        open_ = self.open_

        overdue = self.overdue

        owner_id: str | Unset = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = str(self.owner_id)

        reasons: list[dict[str, Any]] | None | Unset
        if isinstance(self.reasons, Unset):
            reasons = UNSET
        elif isinstance(self.reasons, list):
            reasons = []
            for reasons_type_0_item_data in self.reasons:
                reasons_type_0_item = reasons_type_0_item_data.to_dict()
                reasons.append(reasons_type_0_item)


        else:
            reasons = self.reasons

        stage_count = self.stage_count

        stage_index: int | None | Unset
        if isinstance(self.stage_index, Unset):
            stage_index = UNSET
        else:
            stage_index = self.stage_index

        stage_name: None | str | Unset
        if isinstance(self.stage_name, Unset):
            stage_name = UNSET
        else:
            stage_name = self.stage_name

        total = self.total

        unassigned = self.unassigned


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if active is not UNSET:
            field_dict["active"] = active
        if color_tag is not UNSET:
            field_dict["colorTag"] = color_tag
        if done is not UNSET:
            field_dict["done"] = done
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if health is not UNSET:
            field_dict["health"] = health
        if id is not UNSET:
            field_dict["id"] = id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if lead_user_id is not UNSET:
            field_dict["leadUserId"] = lead_user_id
        if name is not UNSET:
            field_dict["name"] = name
        if open_ is not UNSET:
            field_dict["open"] = open_
        if overdue is not UNSET:
            field_dict["overdue"] = overdue
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if stage_count is not UNSET:
            field_dict["stageCount"] = stage_count
        if stage_index is not UNSET:
            field_dict["stageIndex"] = stage_index
        if stage_name is not UNSET:
            field_dict["stageName"] = stage_name
        if total is not UNSET:
            field_dict["total"] = total
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_project_health_reason_dto import OfficeProjectHealthReasonDto # noqa: PLC0415
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        def _parse_color_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color_tag = _parse_color_tag(d.pop("colorTag", UNSET))


        done = d.pop("done", UNSET)

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)



                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("dueAt", UNSET))


        def _parse_folder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                folder_id_type_0 = UUID(data)



                return folder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        folder_id = _parse_folder_id(d.pop("folderId", UNSET))


        def _parse_health(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        health = _parse_health(d.pop("health", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_archived = d.pop("isArchived", UNSET)

        is_pinned = d.pop("isPinned", UNSET)

        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))


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


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        open_ = d.pop("open", UNSET)

        overdue = d.pop("overdue", UNSET)

        _owner_id = d.pop("ownerId", UNSET)
        owner_id: UUID | Unset
        if isinstance(_owner_id,  Unset):
            owner_id = UNSET
        else:
            owner_id = UUID(_owner_id)




        def _parse_reasons(data: object) -> list[OfficeProjectHealthReasonDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reasons_type_0 = []
                _reasons_type_0 = data
                for reasons_type_0_item_data in (_reasons_type_0):
                    reasons_type_0_item = OfficeProjectHealthReasonDto.from_dict(reasons_type_0_item_data)



                    reasons_type_0.append(reasons_type_0_item)

                return reasons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeProjectHealthReasonDto] | None | Unset, data)

        reasons = _parse_reasons(d.pop("reasons", UNSET))


        stage_count = d.pop("stageCount", UNSET)

        def _parse_stage_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stage_index = _parse_stage_index(d.pop("stageIndex", UNSET))


        def _parse_stage_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_name = _parse_stage_name(d.pop("stageName", UNSET))


        total = d.pop("total", UNSET)

        unassigned = d.pop("unassigned", UNSET)

        office_project_row_dto = cls(
            active=active,
            color_tag=color_tag,
            done=done,
            due_at=due_at,
            folder_id=folder_id,
            health=health,
            id=id,
            is_archived=is_archived,
            is_pinned=is_pinned,
            last_activity_at=last_activity_at,
            lead_user_id=lead_user_id,
            name=name,
            open_=open_,
            overdue=overdue,
            owner_id=owner_id,
            reasons=reasons,
            stage_count=stage_count,
            stage_index=stage_index,
            stage_name=stage_name,
            total=total,
            unassigned=unassigned,
        )

        return office_project_row_dto

