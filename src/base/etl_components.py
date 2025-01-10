# Connector Module
from abc import ABC, abstractmethod


class AbstractConnector(ABC):
    """
    Abstract base class for connectors.

    This class defines the interface for implementing connectors
    that establish connections to external systems or resources.
    """

    @abstractmethod
    def connect(self):
        """
        Establish a connection to the target system or resource.

        This method must be implemented by any subclass to define
        the logic for connecting to a specific system.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        pass


# Extractor Module
from abc import ABC, abstractmethod


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


# Transformer Module
from abc import ABC, abstractmethod


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


# Loader Module
from abc import ABC, abstractmethod


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
