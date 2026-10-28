from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_task_board_column_count_dto import OfficeTaskBoardColumnCountDto
  from ..models.office_task_ungrouped_count_dto import OfficeTaskUngroupedCountDto





T = TypeVar("T", bound="OfficeTaskBoardCountsDto")



@_attrs_define
class OfficeTaskBoardCountsDto:
    

    column_by: None | str | Unset = UNSET
    columns: list[OfficeTaskBoardColumnCountDto] | None | Unset = UNSET
    total: int | Unset = UNSET
    ungrouped_by_list: list[OfficeTaskUngroupedCountDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_board_column_count_dto import OfficeTaskBoardColumnCountDto # noqa: PLC0415
        from ..models.office_task_ungrouped_count_dto import OfficeTaskUngroupedCountDto # noqa: PLC0415
        column_by: None | str | Unset
        if isinstance(self.column_by, Unset):
            column_by = UNSET
        else:
            column_by = self.column_by

        columns: list[dict[str, Any]] | None | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = []
            for columns_type_0_item_data in self.columns:
                columns_type_0_item = columns_type_0_item_data.to_dict()
                columns.append(columns_type_0_item)


        else:
            columns = self.columns

        total = self.total

        ungrouped_by_list: list[dict[str, Any]] | None | Unset
        if isinstance(self.ungrouped_by_list, Unset):
            ungrouped_by_list = UNSET
        elif isinstance(self.ungrouped_by_list, list):
            ungrouped_by_list = []
            for ungrouped_by_list_type_0_item_data in self.ungrouped_by_list:
                ungrouped_by_list_type_0_item = ungrouped_by_list_type_0_item_data.to_dict()
                ungrouped_by_list.append(ungrouped_by_list_type_0_item)


        else:
            ungrouped_by_list = self.ungrouped_by_list


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if column_by is not UNSET:
            field_dict["columnBy"] = column_by
        if columns is not UNSET:
            field_dict["columns"] = columns
        if total is not UNSET:
            field_dict["total"] = total
        if ungrouped_by_list is not UNSET:
            field_dict["ungroupedByList"] = ungrouped_by_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_board_column_count_dto import OfficeTaskBoardColumnCountDto # noqa: PLC0415
        from ..models.office_task_ungrouped_count_dto import OfficeTaskUngroupedCountDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_column_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        column_by = _parse_column_by(d.pop("columnBy", UNSET))


        def _parse_columns(data: object) -> list[OfficeTaskBoardColumnCountDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = []
                _columns_type_0 = data
                for columns_type_0_item_data in (_columns_type_0):
                    columns_type_0_item = OfficeTaskBoardColumnCountDto.from_dict(columns_type_0_item_data)



                    columns_type_0.append(columns_type_0_item)

                return columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskBoardColumnCountDto] | None | Unset, data)

        columns = _parse_columns(d.pop("columns", UNSET))


        total = d.pop("total", UNSET)

        def _parse_ungrouped_by_list(data: object) -> list[OfficeTaskUngroupedCountDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ungrouped_by_list_type_0 = []
                _ungrouped_by_list_type_0 = data
                for ungrouped_by_list_type_0_item_data in (_ungrouped_by_list_type_0):
                    ungrouped_by_list_type_0_item = OfficeTaskUngroupedCountDto.from_dict(ungrouped_by_list_type_0_item_data)



                    ungrouped_by_list_type_0.append(ungrouped_by_list_type_0_item)

                return ungrouped_by_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskUngroupedCountDto] | None | Unset, data)

        ungrouped_by_list = _parse_ungrouped_by_list(d.pop("ungroupedByList", UNSET))


        office_task_board_counts_dto = cls(
            column_by=column_by,
            columns=columns,
            total=total,
            ungrouped_by_list=ungrouped_by_list,
        )

        return office_task_board_counts_dto

