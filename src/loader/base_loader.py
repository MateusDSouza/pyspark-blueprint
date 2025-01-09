# Loader Module
class AbstractLoader(ABC):
    """
    Abstract base class for data loaders.

    This class defines the interface for implementing loaders
    that load data into a target system.
    """

    @abstractmethod
    def load(self, data):
        """
        Load data into the target system.

        This method must be implemented by any subclass to define
        the logic for loading data into a specific target.

        Args:
            data (Any): The data to be loaded.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        pass