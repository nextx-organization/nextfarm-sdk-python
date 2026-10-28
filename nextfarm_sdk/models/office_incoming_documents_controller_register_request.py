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






T = TypeVar("T", bound="OfficeIncomingDocumentsControllerRegisterRequest")



@_attrs_define
class OfficeIncomingDocumentsControllerRegisterRequest:
    

    abstract: None | str | Unset = UNSET
    file_id: None | Unset | UUID = UNSET
    note: None | str | Unset = UNSET
    received_date: datetime.date | None | Unset = UNSET
    register_id: None | Unset | UUID = UNSET
    sender: None | str | Unset = UNSET
    source_date: datetime.date | None | Unset = UNSET
    source_symbol: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        abstract: None | str | Unset
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        else:
            abstract = self.abstract

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        received_date: None | str | Unset
        if isinstance(self.received_date, Unset):
            received_date = UNSET
        elif isinstance(self.received_date, datetime.date):
            received_date = self.received_date.isoformat()
        else:
            received_date = self.received_date

        register_id: None | str | Unset
        if isinstance(self.register_id, Unset):
            register_id = UNSET
        elif isinstance(self.register_id, UUID):
            register_id = str(self.register_id)
        else:
            register_id = self.register_id

        sender: None | str | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        else:
            sender = self.sender

        source_date: None | str | Unset
        if isinstance(self.source_date, Unset):
            source_date = UNSET
        elif isinstance(self.source_date, datetime.date):
            source_date = self.source_date.isoformat()
        else:
            source_date = self.source_date

        source_symbol: None | str | Unset
        if isinstance(self.source_symbol, Unset):
            source_symbol = UNSET
        else:
            source_symbol = self.source_symbol


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if note is not UNSET:
            field_dict["note"] = note
        if received_date is not UNSET:
            field_dict["receivedDate"] = received_date
        if register_id is not UNSET:
            field_dict["registerId"] = register_id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if source_date is not UNSET:
            field_dict["sourceDate"] = source_date
        if source_symbol is not UNSET:
            field_dict["sourceSymbol"] = source_symbol

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_abstract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abstract = _parse_abstract(d.pop("abstract", UNSET))


        def _parse_file_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_id_type_0 = UUID(data)



                return file_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_id = _parse_file_id(d.pop("fileId", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_received_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_date_type_0 = datetime.date.fromisoformat(data)



                return received_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        received_date = _parse_received_date(d.pop("receivedDate", UNSET))


        def _parse_register_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                register_id_type_0 = UUID(data)



                return register_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        register_id = _parse_register_id(d.pop("registerId", UNSET))


        def _parse_sender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender = _parse_sender(d.pop("sender", UNSET))


        def _parse_source_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_date_type_0 = datetime.date.fromisoformat(data)



                return source_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        source_date = _parse_source_date(d.pop("sourceDate", UNSET))


        def _parse_source_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_symbol = _parse_source_symbol(d.pop("sourceSymbol", UNSET))


        office_incoming_documents_controller_register_request = cls(
            abstract=abstract,
            file_id=file_id,
            note=note,
            received_date=received_date,
            register_id=register_id,
            sender=sender,
            source_date=source_date,
            source_symbol=source_symbol,
        )

        return office_incoming_documents_controller_register_request

