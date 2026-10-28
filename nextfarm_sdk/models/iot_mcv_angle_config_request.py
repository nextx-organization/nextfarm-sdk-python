from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IotMcvAngleConfigRequest")



@_attrs_define
class IotMcvAngleConfigRequest:
    

    angle: int | Unset = UNSET
    id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        angle = self.angle

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if angle is not UNSET:
            field_dict["angle"] = angle
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angle = d.pop("angle", UNSET)

        id = d.pop("id", UNSET)

        iot_mcv_angle_config_request = cls(
            angle=angle,
            id=id,
        )

        return iot_mcv_angle_config_request

