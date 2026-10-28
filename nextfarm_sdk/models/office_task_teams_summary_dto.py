from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_department_summary_dto import OfficeTaskDepartmentSummaryDto
  from ..models.office_task_folder_summary_dto import OfficeTaskFolderSummaryDto
  from ..models.office_task_team_summary_dto import OfficeTaskTeamSummaryDto
  from ..models.office_task_unfiled_summary_dto import OfficeTaskUnfiledSummaryDto





T = TypeVar("T", bound="OfficeTaskTeamsSummaryDto")



@_attrs_define
class OfficeTaskTeamsSummaryDto:
    

    departments: list[OfficeTaskDepartmentSummaryDto] | None | Unset = UNSET
    folders: list[OfficeTaskFolderSummaryDto] | None | Unset = UNSET
    teams: list[OfficeTaskTeamSummaryDto] | None | Unset = UNSET
    unfiled: OfficeTaskUnfiledSummaryDto | Unset = UNSET
    view_scope: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_department_summary_dto import OfficeTaskDepartmentSummaryDto # noqa: PLC0415
        from ..models.office_task_folder_summary_dto import OfficeTaskFolderSummaryDto # noqa: PLC0415
        from ..models.office_task_team_summary_dto import OfficeTaskTeamSummaryDto # noqa: PLC0415
        from ..models.office_task_unfiled_summary_dto import OfficeTaskUnfiledSummaryDto # noqa: PLC0415
        departments: list[dict[str, Any]] | None | Unset
        if isinstance(self.departments, Unset):
            departments = UNSET
        elif isinstance(self.departments, list):
            departments = []
            for departments_type_0_item_data in self.departments:
                departments_type_0_item = departments_type_0_item_data.to_dict()
                departments.append(departments_type_0_item)


        else:
            departments = self.departments

        folders: list[dict[str, Any]] | None | Unset
        if isinstance(self.folders, Unset):
            folders = UNSET
        elif isinstance(self.folders, list):
            folders = []
            for folders_type_0_item_data in self.folders:
                folders_type_0_item = folders_type_0_item_data.to_dict()
                folders.append(folders_type_0_item)


        else:
            folders = self.folders

        teams: list[dict[str, Any]] | None | Unset
        if isinstance(self.teams, Unset):
            teams = UNSET
        elif isinstance(self.teams, list):
            teams = []
            for teams_type_0_item_data in self.teams:
                teams_type_0_item = teams_type_0_item_data.to_dict()
                teams.append(teams_type_0_item)


        else:
            teams = self.teams

        unfiled: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unfiled, Unset):
            unfiled = self.unfiled.to_dict()

        view_scope: None | str | Unset
        if isinstance(self.view_scope, Unset):
            view_scope = UNSET
        else:
            view_scope = self.view_scope


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if departments is not UNSET:
            field_dict["departments"] = departments
        if folders is not UNSET:
            field_dict["folders"] = folders
        if teams is not UNSET:
            field_dict["teams"] = teams
        if unfiled is not UNSET:
            field_dict["unfiled"] = unfiled
        if view_scope is not UNSET:
            field_dict["viewScope"] = view_scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_department_summary_dto import OfficeTaskDepartmentSummaryDto # noqa: PLC0415
        from ..models.office_task_folder_summary_dto import OfficeTaskFolderSummaryDto # noqa: PLC0415
        from ..models.office_task_team_summary_dto import OfficeTaskTeamSummaryDto # noqa: PLC0415
        from ..models.office_task_unfiled_summary_dto import OfficeTaskUnfiledSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_departments(data: object) -> list[OfficeTaskDepartmentSummaryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                departments_type_0 = []
                _departments_type_0 = data
                for departments_type_0_item_data in (_departments_type_0):
                    departments_type_0_item = OfficeTaskDepartmentSummaryDto.from_dict(departments_type_0_item_data)



                    departments_type_0.append(departments_type_0_item)

                return departments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskDepartmentSummaryDto] | None | Unset, data)

        departments = _parse_departments(d.pop("departments", UNSET))


        def _parse_folders(data: object) -> list[OfficeTaskFolderSummaryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                folders_type_0 = []
                _folders_type_0 = data
                for folders_type_0_item_data in (_folders_type_0):
                    folders_type_0_item = OfficeTaskFolderSummaryDto.from_dict(folders_type_0_item_data)



                    folders_type_0.append(folders_type_0_item)

                return folders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskFolderSummaryDto] | None | Unset, data)

        folders = _parse_folders(d.pop("folders", UNSET))


        def _parse_teams(data: object) -> list[OfficeTaskTeamSummaryDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                teams_type_0 = []
                _teams_type_0 = data
                for teams_type_0_item_data in (_teams_type_0):
                    teams_type_0_item = OfficeTaskTeamSummaryDto.from_dict(teams_type_0_item_data)



                    teams_type_0.append(teams_type_0_item)

                return teams_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskTeamSummaryDto] | None | Unset, data)

        teams = _parse_teams(d.pop("teams", UNSET))


        _unfiled = d.pop("unfiled", UNSET)
        unfiled: OfficeTaskUnfiledSummaryDto | Unset
        if isinstance(_unfiled,  Unset):
            unfiled = UNSET
        else:
            unfiled = OfficeTaskUnfiledSummaryDto.from_dict(_unfiled)




        def _parse_view_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_scope = _parse_view_scope(d.pop("viewScope", UNSET))


        office_task_teams_summary_dto = cls(
            departments=departments,
            folders=folders,
            teams=teams,
            unfiled=unfiled,
            view_scope=view_scope,
        )

        return office_task_teams_summary_dto

