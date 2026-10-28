from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_office_search_hit import OfficeOfficeSearchHit





T = TypeVar("T", bound="OfficeOfficeModuleSearchResult")



@_attrs_define
class OfficeOfficeModuleSearchResult:
    

    failed: bool | Unset = UNSET
    hits: list[OfficeOfficeSearchHit] | None | Unset = UNSET
    module: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_office_search_hit import OfficeOfficeSearchHit # noqa: PLC0415
        failed = self.failed

        hits: list[dict[str, Any]] | None | Unset
        if isinstance(self.hits, Unset):
            hits = UNSET
        elif isinstance(self.hits, list):
            hits = []
            for hits_type_0_item_data in self.hits:
                hits_type_0_item = hits_type_0_item_data.to_dict()
                hits.append(hits_type_0_item)


        else:
            hits = self.hits

        module: None | str | Unset
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if failed is not UNSET:
            field_dict["failed"] = failed
        if hits is not UNSET:
            field_dict["hits"] = hits
        if module is not UNSET:
            field_dict["module"] = module

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_office_search_hit import OfficeOfficeSearchHit # noqa: PLC0415
        d = dict(src_dict)
        failed = d.pop("failed", UNSET)

        def _parse_hits(data: object) -> list[OfficeOfficeSearchHit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hits_type_0 = []
                _hits_type_0 = data
                for hits_type_0_item_data in (_hits_type_0):
                    hits_type_0_item = OfficeOfficeSearchHit.from_dict(hits_type_0_item_data)



                    hits_type_0.append(hits_type_0_item)

                return hits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeOfficeSearchHit] | None | Unset, data)

        hits = _parse_hits(d.pop("hits", UNSET))


        def _parse_module(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        module = _parse_module(d.pop("module", UNSET))


        office_office_module_search_result = cls(
            failed=failed,
            hits=hits,
            module=module,
        )

        return office_office_module_search_result

