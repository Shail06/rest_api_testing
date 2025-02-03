import uuid

class SoftAssert:
    def __init__(self):
        self.errors = []

    def soft_assert(self, assert_condition, message):
        if not assert_condition:
            self.errors.append(message)
            
    def assert_valid_uuid(self, value, message="Invalid UUID format"):
        try:
            assert isinstance(value, str)
            uuid.UUID(value)
        except(AssertionError, ValueError) as e:
            self.errors.append(f"{message}: {e}")
            
            
    def assert_all(self):
        """
        Raises all collected assertion errors if any, at the end of the scenario.
        """
        if self.errors:
            raise AssertionError("\n".join(self.errors))