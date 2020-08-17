from project.hardware.hardware import Hardware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software
from typing import List


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        new = PowerHardware(name, capacity, memory)
        System._hardware.append(new)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        new = HeavyHardware(name, capacity, memory)
        System._hardware.append(new)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        hardware = hardware[0]
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
        except Exception:
            return "Software cannot be installed"
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [hard for hard in System._hardware if hard.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        hardware = hardware[0]
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(software)
        except Exception:
            return "Software cannot be installed"
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware_name_ll = [h for h in System._hardware if h.name == hardware_name]

        if not hardware_name_ll:
            return f'Some of the components do not exist'
        hardware_name_ll = hardware_name_ll[0]
        software_name_ll = [s for s in hardware_name_ll.software_components if s.name == software_name]
        if not software_name_ll:
            return f'Some of the components do not exist'
        software_name_ll = software_name_ll[0]
        hardware_name_ll.uninstall(software_name_ll)
        System._software.remove(software_name_ll)

    @staticmethod
    def analyze():
        result = f'System Analysis\nHardware Components: {len(System._hardware)}\n' \
                 f'Software Components: {len(System._software)}\n' \

        total_used_memory = int(sum([m.used_memory for m in System._hardware]))
        total_memory = int(sum([m.memory for m in System._hardware]))

        total_used_capacity = int(sum([c.used_capacity for c in System._hardware]))
        total_capacity = int(sum([c.capacity for c in System._hardware]))

        result += f'Total Operational Memory: {total_used_memory} / {total_memory}\n' \
                  f'Total Capacity Taken: {total_used_capacity} / {total_capacity}'

        return result

    @staticmethod
    def system_split():
        result = f''
        for hardware in System._hardware:
            express_software = [soft for soft in hardware.software_components
                                if soft.__class__.__name__ == 'ExpressSoftware']
            light_software = [soft for soft in hardware.software_components
                              if soft.__class__.__name__ == 'LightSoftware']

            memory_usage = int(hardware.used_memory)
            total_memory = int(hardware.memory)
            capacity_usage = int(hardware.used_capacity)
            total_capacity = int(hardware.capacity)
            type = {'HeavyHardware': 'Heavy', 'PowerHardware': 'Power'}
            software_components = ", ".join(soft.name for soft in hardware.software_components)

            result += f'Hardware Component - {hardware.name}\n' \
                      f'Express Software Components: {len(express_software)}\n' \
                      f'Light Software Components: {len(light_software)}\n' \
                      f'Memory Usage: {memory_usage} / {total_memory}\n' \
                      f'Capacity Usage: {capacity_usage} / {total_capacity}\n' \
                      f'Type: {type[hardware.__class__.__name__]}\n' \
                      f'Software Components: {software_components if software_components else "None"}'

        return result