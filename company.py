from load_files import update_data
class company:
    """
    Represents a Company
    """
    def __init__(self, id: str):
        self.id = id
        update_data(id)
