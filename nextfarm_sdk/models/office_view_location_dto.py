from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeViewLocationDto")



@_attrs_define
class OfficeViewLocationDto:
    

    app_id: UUID | Unset = UNSET
    app_name: None | str | Unset = UNSET
    table_id: UUID | Unset = UNSET
    table_name: None | str | Unset = UNSET
    view_id: UUID | Unset = UNSET
    view_name: None | str | Unset = UNSET
    view_type: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        app_name: None | str | Unset
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)

        table_name: None | str | Unset
        if isinstance(self.table_name, Unset):
            table_name = UNSET
        else:
            table_name = self.table_name

        view_id: str | Unset = UNSET
        if not isinstance(self.view_id, Unset):
            view_id = str(self.view_id)

        view_name: None | str | Unset
        if isinstance(self.view_name, Unset):
            view_name = UNSET
        else:
            view_name = self.view_name

        view_type: None | str | Unset
        if isinstance(self.view_type, Unset):
            view_type = UNSET
        else:
            view_type = self.view_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if view_id is not UNSET:
            field_dict["viewId"] = view_id
        if view_name is not UNSET:
            field_dict["viewName"] = view_name
        if view_type is not UNSET:
            field_dict["viewType"] = view_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _app_id = d.pop("appId", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id,  Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)




        def _parse_app_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_name = _parse_app_name(d.pop("appName", UNSET))


        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id,  Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)




        def _parse_table_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_name = _parse_table_name(d.pop("tableName", UNSET))


        _view_id = d.pop("viewId", UNSET)
        view_id: UUID | Unset
        if isinstance(_view_id,  Unset):
            view_id = UNSET
        else:
            view_id = UUID(_view_id)




        def _parse_view_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_name = _parse_view_name(d.pop("viewName", UNSET))


        def _parse_view_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        view_type = _parse_view_type(d.pop("viewType", UNSET))


        office_view_location_dto = cls(
            app_id=app_id,
            app_name=app_name,
            table_id=table_id,
            table_name=table_name,
            view_id=view_id,
            view_name=view_name,
            view_type=view_type,
        )

        return office_view_location_dto

