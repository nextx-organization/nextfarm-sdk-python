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






T = TypeVar("T", bound="OfficeIncomingDocumentsControllerAssignRequest")



@_attrs_define
class OfficeIncomingDocumentsControllerAssignRequest:
    

    handler_id: None | Unset | UUID = UNSET
    handling_unit: None | str | Unset = UNSET
    resolve_due_date: datetime.date | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        handler_id: None | str | Unset
        if isinstance(self.handler_id, Unset):
            handler_id = UNSET
        elif isinstance(self.handler_id, UUID):
            handler_id = str(self.handler_id)
        else:
            handler_id = self.handler_id

        handling_unit: None | str | Unset
        if isinstance(self.handling_unit, Unset):
            handling_unit = UNSET
        else:
            handling_unit = self.handling_unit

        resolve_due_date: None | str | Unset
        if isinstance(self.resolve_due_date, Unset):
            resolve_due_date = UNSET
        elif isinstance(self.resolve_due_date, datetime.date):
            resolve_due_date = self.resolve_due_date.isoformat()
        else:
            resolve_due_date = self.resolve_due_date


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if handler_id is not UNSET:
            field_dict["handlerId"] = handler_id
        if handling_unit is not UNSET:
            field_dict["handlingUnit"] = handling_unit
        if resolve_due_date is not UNSET:
            field_dict["resolveDueDate"] = resolve_due_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_handler_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                handler_id_type_0 = UUID(data)



                return handler_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        handler_id = _parse_handler_id(d.pop("handlerId", UNSET))


        def _parse_handling_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handling_unit = _parse_handling_unit(d.pop("handlingUnit", UNSET))


        def _parse_resolve_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolve_due_date_type_0 = datetime.date.fromisoformat(data)



                return resolve_due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        resolve_due_date = _parse_resolve_due_date(d.pop("resolveDueDate", UNSET))


        office_incoming_documents_controller_assign_request = cls(
            handler_id=handler_id,
            handling_unit=handling_unit,
            resolve_due_date=resolve_due_date,
        )

        return office_incoming_documents_controller_assign_request

