from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_record_filter import OfficeRecordFilter





T = TypeVar("T", bound="OfficeFindReplaceRequest")



@_attrs_define
class OfficeFindReplaceRequest:
    

    dry_run: bool | Unset = UNSET
    field_ids: list[UUID] | None | Unset = UNSET
    filter_: OfficeRecordFilter | Unset = UNSET
    find: None | str | Unset = UNSET
    match_case: bool | Unset = UNSET
    replace: None | str | Unset = UNSET
    whole_cell: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        dry_run = self.dry_run

        field_ids: list[str] | None | Unset
        if isinstance(self.field_ids, Unset):
            field_ids = UNSET
        elif isinstance(self.field_ids, list):
            field_ids = []
            for field_ids_type_0_item_data in self.field_ids:
                field_ids_type_0_item = str(field_ids_type_0_item_data)
                field_ids.append(field_ids_type_0_item)


        else:
            field_ids = self.field_ids

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        find: None | str | Unset
        if isinstance(self.find, Unset):
            find = UNSET
        else:
            find = self.find

        match_case = self.match_case

        replace: None | str | Unset
        if isinstance(self.replace, Unset):
            replace = UNSET
        else:
            replace = self.replace

        whole_cell = self.whole_cell


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if field_ids is not UNSET:
            field_dict["fieldIds"] = field_ids
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if find is not UNSET:
            field_dict["find"] = find
        if match_case is not UNSET:
            field_dict["matchCase"] = match_case
        if replace is not UNSET:
            field_dict["replace"] = replace
        if whole_cell is not UNSET:
            field_dict["wholeCell"] = whole_cell

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_record_filter import OfficeRecordFilter # noqa: PLC0415
        d = dict(src_dict)
        dry_run = d.pop("dryRun", UNSET)

        def _parse_field_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                field_ids_type_0 = []
                _field_ids_type_0 = data
                for field_ids_type_0_item_data in (_field_ids_type_0):
                    field_ids_type_0_item = UUID(field_ids_type_0_item_data)



                    field_ids_type_0.append(field_ids_type_0_item)

                return field_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        field_ids = _parse_field_ids(d.pop("fieldIds", UNSET))


        _filter_ = d.pop("filter", UNSET)
        filter_: OfficeRecordFilter | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = OfficeRecordFilter.from_dict(_filter_)




        def _parse_find(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        find = _parse_find(d.pop("find", UNSET))


        match_case = d.pop("matchCase", UNSET)

        def _parse_replace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replace = _parse_replace(d.pop("replace", UNSET))


        whole_cell = d.pop("wholeCell", UNSET)

        office_find_replace_request = cls(
            dry_run=dry_run,
            field_ids=field_ids,
            filter_=filter_,
            find=find,
            match_case=match_case,
            replace=replace,
            whole_cell=whole_cell,
        )

        return office_find_replace_request

