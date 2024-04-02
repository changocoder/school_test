from enum import Enum


class AbsenceReasonEnum(Enum):
    """Enum para los motivos de ausencia."""

    ILLNESS = "illness"
    PERSONAL_MATTER = "personal matter"
    MEDICAL_APPOINTMENT = "medical appointment"
    RAINY_DAY = "rainy day"
    OTHER = "other"
