from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ReportReportPeriod")



@_attrs_define
class ReportReportPeriod:
    

    compare_from: datetime.date | None | Unset = UNSET
    compare_to: datetime.date | None | Unset = UNSET
    from_: datetime.date | Unset = UNSET
    grain: None | str | Unset = UNSET
    to: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        compare_from: None | str | Unset
        if isinstance(self.compare_from, Unset):
            compare_from = UNSET
        elif isinstance(self.compare_from, datetime.date):
            compare_from = self.compare_from.isoformat()
        else:
            compare_from = self.compare_from

        compare_to: None | str | Unset
        if isinstance(self.compare_to, Unset):
            compare_to = UNSET
        elif isinstance(self.compare_to, datetime.date):
            compare_to = self.compare_to.isoformat()
        else:
            compare_to = self.compare_to

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        grain: None | str | Unset
        if isinstance(self.grain, Unset):
            grain = UNSET
        else:
            grain = self.grain

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if compare_from is not UNSET:
            field_dict["compareFrom"] = compare_from
        if compare_to is not UNSET:
            field_dict["compareTo"] = compare_to
        if from_ is not UNSET:
            field_dict["from"] = from_
        if grain is not UNSET:
            field_dict["grain"] = grain
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_compare_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compare_from_type_0 = datetime.date.fromisoformat(data)



                return compare_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        compare_from = _parse_compare_from(d.pop("compareFrom", UNSET))


        def _parse_compare_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compare_to_type_0 = datetime.date.fromisoformat(data)



                return compare_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        compare_to = _parse_compare_to(d.pop("compareTo", UNSET))


        _from_ = d.pop("from", UNSET)
        from_: datetime.date | Unset
        if isinstance(_from_,  Unset):
            from_ = UNSET
        else:
            from_ = datetime.date.fromisoformat(_from_)




        def _parse_grain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grain = _parse_grain(d.pop("grain", UNSET))


        _to = d.pop("to", UNSET)
        to: datetime.date | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = datetime.date.fromisoformat(_to)




        report_report_period = cls(
            compare_from=compare_from,
            compare_to=compare_to,
            from_=from_,
            grain=grain,
            to=to,
        )

        return report_report_period

