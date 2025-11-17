from dataclasses import dataclass

@dataclass
class ServiceError(Exception):
    status_code: int
    detail: str

