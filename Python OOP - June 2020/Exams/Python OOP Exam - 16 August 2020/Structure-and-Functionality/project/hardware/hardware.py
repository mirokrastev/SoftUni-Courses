from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_capacity = 0
        self.used_memory = 0

    def install(self, software: Software):
        if software.memory_consumption + self.used_memory > self.memory or \
                software.capacity_consumption + self.used_capacity > self.capacity:
            raise Exception('Software cannot be installed')
        self.software_components.append(software)
        self.used_capacity += software.capacity_consumption
        self.used_memory += software.memory_consumption

    def uninstall(self, software: Software):
        if software not in self.software_components: return
        self.software_components.remove(software)
        self.used_capacity -= software.capacity_consumption
        self.used_memory -= software.memory_consumption