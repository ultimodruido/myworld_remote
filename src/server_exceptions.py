class UnknownFrequencyError(Exception):
    message: str = "Unknown frequency code"


class UnknownTrainError(Exception):
    message: str = "Train not found"
