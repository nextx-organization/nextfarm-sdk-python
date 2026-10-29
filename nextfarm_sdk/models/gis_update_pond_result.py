from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisUpdatePondResult")



@_attrs_define
class GisUpdatePondResult:
    

    branch_id: None | Unset | UUID = UNSET
    pond_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        pond_id: str | Unset = UNSET
        if not isinstance(self.pond_id, Unset):
            pond_id = str(self.pond_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if pond_id is not UNSET:
            field_dict["pond_id"] = pond_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branch_id", UNSET))


        _pond_id = d.pop("pond_id", UNSET)
        pond_id: UUID | Unset
        if isinstance(_pond_id,  Unset):
            pond_id = UNSET
        else:
            pond_id = UUID(_pond_id)




        gis_update_pond_result = cls(
            branch_id=branch_id,
            pond_id=pond_id,
        )

        return gis_update_pond_result

