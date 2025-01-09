# Transformer Module
class AbstractTransform(ABC):
    """
    Abstract base class for data transformers.

    This class defines the interface for implementing transformers
    that process and transform data.

    Attributes:
        data (Any): The data to be transformed.
    """

    def __init__(self, data):
        """
        Initialize the transformer with data.

        Args:
            data (Any): The data to be transformed.
        """
        self.data = data

    @abstractmethod
    def transform(self):
        """
        Transform the data.

        This method must be implemented by any subclass to define
        the logic for transforming data.

        Returns:
            Any: The transformed data.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        pass