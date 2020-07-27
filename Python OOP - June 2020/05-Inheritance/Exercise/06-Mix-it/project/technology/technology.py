from project.capacity_mixin import CapacityMixin


class Technology(CapacityMixin):
    def __init__(self, memory: float, memory_taken: float):
        self.memory = memory
        self.memory_taken = memory_taken
