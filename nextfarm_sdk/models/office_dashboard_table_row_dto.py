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
  from ..models.office_dashboard_table_row_dto_cells_type_0 import OfficeDashboardTableRowDtoCellsType0





T = TypeVar("T", bound="OfficeDashboardTableRowDto")



@_attrs_define
class OfficeDashboardTableRowDto:
    

    cells: None | OfficeDashboardTableRowDtoCellsType0 | Unset = UNSET
    record_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_dashboard_table_row_dto_cells_type_0 import OfficeDashboardTableRowDtoCellsType0 # noqa: PLC0415
        cells: dict[str, Any] | None | Unset
        if isinstance(self.cells, Unset):
            cells = UNSET
        elif isinstance(self.cells, OfficeDashboardTableRowDtoCellsType0):
            cells = self.cells.to_dict()
        else:
            cells = self.cells

        record_id: str | Unset = UNSET
        if not isinstance(self.record_id, Unset):
            record_id = str(self.record_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cells is not UNSET:
            field_dict["cells"] = cells
        if record_id is not UNSET:
            field_dict["recordId"] = record_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_dashboard_table_row_dto_cells_type_0 import OfficeDashboardTableRowDtoCellsType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_cells(data: object) -> None | OfficeDashboardTableRowDtoCellsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cells_type_0 = OfficeDashboardTableRowDtoCellsType0.from_dict(data)



                return cells_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeDashboardTableRowDtoCellsType0 | Unset, data)

        cells = _parse_cells(d.pop("cells", UNSET))


        _record_id = d.pop("recordId", UNSET)
        record_id: UUID | Unset
        if isinstance(_record_id,  Unset):
            record_id = UNSET
        else:
            record_id = UUID(_record_id)




        office_dashboard_table_row_dto = cls(
            cells=cells,
            record_id=record_id,
        )

        return office_dashboard_table_row_dto

