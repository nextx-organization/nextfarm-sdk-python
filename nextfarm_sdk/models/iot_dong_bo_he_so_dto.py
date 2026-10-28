from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="IotDongBoHeSoDto")



@_attrs_define
class IotDongBoHeSoDto:
    

    da_gui: int | None | Unset = UNSET
    echo_luc: datetime.datetime | None | Unset = UNSET
    gui_luc: datetime.datetime | None | Unset = UNSET
    trang_thai: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        da_gui: int | None | Unset
        if isinstance(self.da_gui, Unset):
            da_gui = UNSET
        else:
            da_gui = self.da_gui

        echo_luc: None | str | Unset
        if isinstance(self.echo_luc, Unset):
            echo_luc = UNSET
        elif isinstance(self.echo_luc, datetime.datetime):
            echo_luc = self.echo_luc.isoformat()
        else:
            echo_luc = self.echo_luc

        gui_luc: None | str | Unset
        if isinstance(self.gui_luc, Unset):
            gui_luc = UNSET
        elif isinstance(self.gui_luc, datetime.datetime):
            gui_luc = self.gui_luc.isoformat()
        else:
            gui_luc = self.gui_luc

        trang_thai: None | str | Unset
        if isinstance(self.trang_thai, Unset):
            trang_thai = UNSET
        else:
            trang_thai = self.trang_thai


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if da_gui is not UNSET:
            field_dict["da_gui"] = da_gui
        if echo_luc is not UNSET:
            field_dict["echo_luc"] = echo_luc
        if gui_luc is not UNSET:
            field_dict["gui_luc"] = gui_luc
        if trang_thai is not UNSET:
            field_dict["trang_thai"] = trang_thai

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_da_gui(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        da_gui = _parse_da_gui(d.pop("da_gui", UNSET))


        def _parse_echo_luc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                echo_luc_type_0 = datetime.datetime.fromisoformat(data)



                return echo_luc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        echo_luc = _parse_echo_luc(d.pop("echo_luc", UNSET))


        def _parse_gui_luc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gui_luc_type_0 = datetime.datetime.fromisoformat(data)



                return gui_luc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        gui_luc = _parse_gui_luc(d.pop("gui_luc", UNSET))


        def _parse_trang_thai(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trang_thai = _parse_trang_thai(d.pop("trang_thai", UNSET))


        iot_dong_bo_he_so_dto = cls(
            da_gui=da_gui,
            echo_luc=echo_luc,
            gui_luc=gui_luc,
            trang_thai=trang_thai,
        )

        return iot_dong_bo_he_so_dto

