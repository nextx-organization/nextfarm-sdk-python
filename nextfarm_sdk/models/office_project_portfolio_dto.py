from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.office_project_portfolio_kpis_dto import OfficeProjectPortfolioKpisDto
  from ..models.office_project_row_dto import OfficeProjectRowDto





T = TypeVar("T", bound="OfficeProjectPortfolioDto")



@_attrs_define
class OfficeProjectPortfolioDto:
    

    generated_at: datetime.datetime | Unset = UNSET
    kpis: OfficeProjectPortfolioKpisDto | Unset = UNSET
    projects: list[OfficeProjectRowDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_project_portfolio_kpis_dto import OfficeProjectPortfolioKpisDto # noqa: PLC0415
        from ..models.office_project_row_dto import OfficeProjectRowDto # noqa: PLC0415
        generated_at: str | Unset = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat()

        kpis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kpis, Unset):
            kpis = self.kpis.to_dict()

        projects: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)


        else:
            projects = self.projects


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at
        if kpis is not UNSET:
            field_dict["kpis"] = kpis
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_project_portfolio_kpis_dto import OfficeProjectPortfolioKpisDto # noqa: PLC0415
        from ..models.office_project_row_dto import OfficeProjectRowDto # noqa: PLC0415
        d = dict(src_dict)
        _generated_at = d.pop("generatedAt", UNSET)
        generated_at: datetime.datetime | Unset
        if isinstance(_generated_at,  Unset):
            generated_at = UNSET
        else:
            generated_at = datetime.datetime.fromisoformat(_generated_at)




        _kpis = d.pop("kpis", UNSET)
        kpis: OfficeProjectPortfolioKpisDto | Unset
        if isinstance(_kpis,  Unset):
            kpis = UNSET
        else:
            kpis = OfficeProjectPortfolioKpisDto.from_dict(_kpis)




        def _parse_projects(data: object) -> list[OfficeProjectRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in (_projects_type_0):
                    projects_type_0_item = OfficeProjectRowDto.from_dict(projects_type_0_item_data)



                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeProjectRowDto] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))


        office_project_portfolio_dto = cls(
            generated_at=generated_at,
            kpis=kpis,
            projects=projects,
        )

        return office_project_portfolio_dto

