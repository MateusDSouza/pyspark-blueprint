# Connector Module
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
