from dataclasses import dataclass


@dataclass
class AppConfig:
    port: int
    debug: bool
