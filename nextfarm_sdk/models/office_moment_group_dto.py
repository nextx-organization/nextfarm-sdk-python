from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_moment_dto import OfficeMomentDto





T = TypeVar("T", bound="OfficeMomentGroupDto")



@_attrs_define
class OfficeMomentGroupDto:
    

    author_id: UUID | Unset = UNSET
    has_unviewed: bool | Unset = UNSET
    latest_at: datetime.datetime | Unset = UNSET
    moments: list[OfficeMomentDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_moment_dto import OfficeMomentDto # noqa: PLC0415
        author_id: str | Unset = UNSET
        if not isinstance(self.author_id, Unset):
            author_id = str(self.author_id)

        has_unviewed = self.has_unviewed

        latest_at: str | Unset = UNSET
        if not isinstance(self.latest_at, Unset):
            latest_at = self.latest_at.isoformat()

        moments: list[dict[str, Any]] | None | Unset
        if isinstance(self.moments, Unset):
            moments = UNSET
        elif isinstance(self.moments, list):
            moments = []
            for moments_type_0_item_data in self.moments:
                moments_type_0_item = moments_type_0_item_data.to_dict()
                moments.append(moments_type_0_item)


        else:
            moments = self.moments


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if has_unviewed is not UNSET:
            field_dict["hasUnviewed"] = has_unviewed
        if latest_at is not UNSET:
            field_dict["latestAt"] = latest_at
        if moments is not UNSET:
            field_dict["moments"] = moments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_moment_dto import OfficeMomentDto # noqa: PLC0415
        d = dict(src_dict)
        _author_id = d.pop("authorId", UNSET)
        author_id: UUID | Unset
        if isinstance(_author_id,  Unset):
            author_id = UNSET
        else:
            author_id = UUID(_author_id)




        has_unviewed = d.pop("hasUnviewed", UNSET)

        _latest_at = d.pop("latestAt", UNSET)
        latest_at: datetime.datetime | Unset
        if isinstance(_latest_at,  Unset):
            latest_at = UNSET
        else:
            latest_at = datetime.datetime.fromisoformat(_latest_at)




        def _parse_moments(data: object) -> list[OfficeMomentDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                moments_type_0 = []
                _moments_type_0 = data
                for moments_type_0_item_data in (_moments_type_0):
                    moments_type_0_item = OfficeMomentDto.from_dict(moments_type_0_item_data)



                    moments_type_0.append(moments_type_0_item)

                return moments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeMomentDto] | None | Unset, data)

        moments = _parse_moments(d.pop("moments", UNSET))


        office_moment_group_dto = cls(
            author_id=author_id,
            has_unviewed=has_unviewed,
            latest_at=latest_at,
            moments=moments,
        )

        return office_moment_group_dto

