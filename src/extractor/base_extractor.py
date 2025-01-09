# Extractor Module
class AbstractExtractor(ABC):
    """
    Abstract base class for extractors.

    This class defines the interface for implementing extractors
    that retrieve data from a source.
    """

    @abstractmethod
    def extract(self):
        """
        Extract data from the source.

        This method must be implemented by any subclass to define
        the logic for retrieving data from a specific source.

        Returns:
            Any: The extracted data.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        pass