from typing import Literal

OfficeQuestionSummaryDtoStatus = Literal['Answered', 'Closed', 'Open', 'Resolved']

OFFICE_QUESTION_SUMMARY_DTO_STATUS_VALUES: set[OfficeQuestionSummaryDtoStatus] = { 'Answered', 'Closed', 'Open', 'Resolved',  }

def check_office_question_summary_dto_status(value: str) -> OfficeQuestionSummaryDtoStatus:
    if value in OFFICE_QUESTION_SUMMARY_DTO_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_QUESTION_SUMMARY_DTO_STATUS_VALUES!r}")
