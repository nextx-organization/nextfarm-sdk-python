from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeImportMeetingArtifactsResultDto")



@_attrs_define
class OfficeImportMeetingArtifactsResultDto:
    

    found_something: bool | Unset = UNSET
    has_recording: bool | Unset = UNSET
    has_transcript: bool | Unset = UNSET
    outcome: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        found_something = self.found_something

        has_recording = self.has_recording

        has_transcript = self.has_transcript

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        else:
            outcome = self.outcome


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if found_something is not UNSET:
            field_dict["foundSomething"] = found_something
        if has_recording is not UNSET:
            field_dict["hasRecording"] = has_recording
        if has_transcript is not UNSET:
            field_dict["hasTranscript"] = has_transcript
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        found_something = d.pop("foundSomething", UNSET)

        has_recording = d.pop("hasRecording", UNSET)

        has_transcript = d.pop("hasTranscript", UNSET)

        def _parse_outcome(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome = _parse_outcome(d.pop("outcome", UNSET))


        office_import_meeting_artifacts_result_dto = cls(
            found_something=found_something,
            has_recording=has_recording,
            has_transcript=has_transcript,
            outcome=outcome,
        )

        return office_import_meeting_artifacts_result_dto

