from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.gis_metric_scope_dto import GisMetricScopeDto





T = TypeVar("T", bound="GisMetricQueryItem")



@_attrs_define
class GisMetricQueryItem:
    

    code: None | str | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    key: None | str | Unset = UNSET
    scope: GisMetricScopeDto | Unset = UNSET
    to: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.gis_metric_scope_dto import GisMetricScopeDto # noqa: PLC0415
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if from_ is not UNSET:
            field_dict["from"] = from_
        if key is not UNSET:
            field_dict["key"] = key
        if scope is not UNSET:
            field_dict["scope"] = scope
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gis_metric_scope_dto import GisMetricScopeDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))


        _scope = d.pop("scope", UNSET)
        scope: GisMetricScopeDto | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = GisMetricScopeDto.from_dict(_scope)




        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        gis_metric_query_item = cls(
            code=code,
            from_=from_,
            key=key,
            scope=scope,
            to=to,
        )

        return gis_metric_query_item

