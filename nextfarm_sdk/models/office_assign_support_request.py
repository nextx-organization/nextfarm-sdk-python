from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeAssignSupportRequest")



@_attrs_define
class OfficeAssignSupportRequest:
    

    nguoi_nhan: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        nguoi_nhan: None | str | Unset
        if isinstance(self.nguoi_nhan, Unset):
            nguoi_nhan = UNSET
        elif isinstance(self.nguoi_nhan, UUID):
            nguoi_nhan = str(self.nguoi_nhan)
        else:
            nguoi_nhan = self.nguoi_nhan


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if nguoi_nhan is not UNSET:
            field_dict["nguoiNhan"] = nguoi_nhan

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_nguoi_nhan(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nguoi_nhan_type_0 = UUID(data)



                return nguoi_nhan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        nguoi_nhan = _parse_nguoi_nhan(d.pop("nguoiNhan", UNSET))


        office_assign_support_request = cls(
            nguoi_nhan=nguoi_nhan,
        )

        return office_assign_support_request

