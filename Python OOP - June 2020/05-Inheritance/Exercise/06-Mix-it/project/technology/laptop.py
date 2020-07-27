from project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory: float, memory_taken: float):
        super().__init__(memory, memory_taken)

    def install_software(self, software, software_memory):
        memory_left = self.get_capacity(self.memory, self.memory_taken + software_memory)
        if memory_left != "Capacity reached!":
            self.memory_taken += software_memory
            return memory_left
        return f"You don't have enough space for {software}!"
