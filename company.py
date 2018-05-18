from load_files import update_data
class Company:
    """
    Represents a Company
    """
    def __init__(self, id: str):
        """
        Initialize a new company
        """
        self.id = id
        self.storage = []
        update_data(id)

