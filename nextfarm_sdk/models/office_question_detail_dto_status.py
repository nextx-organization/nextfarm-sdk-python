from typing import Literal

OfficeQuestionDetailDtoStatus = Literal['Answered', 'Closed', 'Open', 'Resolved']

OFFICE_QUESTION_DETAIL_DTO_STATUS_VALUES: set[OfficeQuestionDetailDtoStatus] = { 'Answered', 'Closed', 'Open', 'Resolved',  }

def check_office_question_detail_dto_status(value: str) -> OfficeQuestionDetailDtoStatus:
    if value in OFFICE_QUESTION_DETAIL_DTO_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OFFICE_QUESTION_DETAIL_DTO_STATUS_VALUES!r}")
