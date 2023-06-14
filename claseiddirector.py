class IDirector(ABC):

    @abstractmethod
    def modificar_basico(self, dni, nuevo_basico):
        pass

    @abstractmethod
    def modificar_porcentaje_por_cargo(self, dni, nuevo_porcentaje):
        pass

    @abstractmethod
    def modificar_porcentaje_por_categoria(self, dni, nuevo_porcentaje):
        pass

    @abstractmethod
    def modificar_importe_extra(self, dni, nuevo_importe_extra):
        pass
