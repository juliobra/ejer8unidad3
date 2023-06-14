class ITesorero(ABC):

    @abstractmethod
    def gastos_sueldo_por_empleado(self, dni):
        pass