from sqlmodel import Session


class BaseRepo:
    def __init__(self, session: Session) -> None:
        self.session = session
