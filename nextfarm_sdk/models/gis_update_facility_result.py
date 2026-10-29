from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GisUpdateFacilityResult")



@_attrs_define
class GisUpdateFacilityResult:
    

    branch_id: None | Unset | UUID = UNSET
    facility_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        facility_id: str | Unset = UNSET
        if not isinstance(self.facility_id, Unset):
            facility_id = str(self.facility_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if branch_id is not UNSET:
            field_dict["branch_id"] = branch_id
        if facility_id is not UNSET:
            field_dict["facility_id"] = facility_id

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


        _facility_id = d.pop("facility_id", UNSET)
        facility_id: UUID | Unset
        if isinstance(_facility_id,  Unset):
            facility_id = UNSET
        else:
            facility_id = UUID(_facility_id)




        gis_update_facility_result = cls(
            branch_id=branch_id,
            facility_id=facility_id,
        )

        return gis_update_facility_result

