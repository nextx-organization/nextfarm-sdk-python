from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_ai_column_mode_dto import OfficeAiColumnModeDto





T = TypeVar("T", bound="OfficeAiColumnCatalogDto")



@_attrs_define
class OfficeAiColumnCatalogDto:
    

    available: bool | Unset = UNSET
    modes: list[OfficeAiColumnModeDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_ai_column_mode_dto import OfficeAiColumnModeDto # noqa: PLC0415
        available = self.available

        modes: list[dict[str, Any]] | None | Unset
        if isinstance(self.modes, Unset):
            modes = UNSET
        elif isinstance(self.modes, list):
            modes = []
            for modes_type_0_item_data in self.modes:
                modes_type_0_item = modes_type_0_item_data.to_dict()
                modes.append(modes_type_0_item)


        else:
            modes = self.modes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available
        if modes is not UNSET:
            field_dict["modes"] = modes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_ai_column_mode_dto import OfficeAiColumnModeDto # noqa: PLC0415
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        def _parse_modes(data: object) -> list[OfficeAiColumnModeDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modes_type_0 = []
                _modes_type_0 = data
                for modes_type_0_item_data in (_modes_type_0):
                    modes_type_0_item = OfficeAiColumnModeDto.from_dict(modes_type_0_item_data)



                    modes_type_0.append(modes_type_0_item)

                return modes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAiColumnModeDto] | None | Unset, data)

        modes = _parse_modes(d.pop("modes", UNSET))


        office_ai_column_catalog_dto = cls(
            available=available,
            modes=modes,
        )

        return office_ai_column_catalog_dto

