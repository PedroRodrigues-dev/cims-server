import psutil
from tools import threadMonitor


commandDict = {
    "help": "Show the list of all commands",
    "diskInfo": "Show disk informations",
    "memoryInfo": "Show memory informations",
    "cpuInfo": "Show cpu informations",
    "showRoutines": "Show timelang routines",
}


def help():
    return "\n".join([f"{k}: {v}" for k, v in commandDict.items()])


def diskInfo():
    disk_info = ""

    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            partition_info = psutil.disk_usage(partition.mountpoint)
            total_space_gb = round(partition_info.total / (1024**3), 2)
            used_space_gb = round(partition_info.used / (1024**3), 2)
            free_space_gb = round(partition_info.free / (1024**3), 2)
            usage_percentage = round(partition_info.percent, 2)

            disk_info += (
                f"Device: {partition.device}\n"
                f"File System: {partition.fstype}\n"
                f"Total Space: {total_space_gb}GB\n"
                f"Used Space: {used_space_gb}GB\n"
                f"Free Space: {free_space_gb}GB\n"
                f"Usage: {usage_percentage}%\n\n"
            )
    except Exception as e:
        print(f"Failed to get disk information: {e}")

    if not disk_info:
        disk_info = "No disk was found"

    return disk_info


def memoryInfo():
    memory_info = ""

    try:
        virtual_memory = psutil.virtual_memory()
        total_ram_gb = round(virtual_memory.total / (1024**3), 2)
        used_ram_gb = round(virtual_memory.used / (1024**3), 2)
        free_ram_gb = round(virtual_memory.available / (1024**3), 2)
        usage_percentage = round(virtual_memory.percent, 2)

        memory_info = (
            f"Total RAM: {total_ram_gb}GB\n"
            f"Used RAM: {used_ram_gb}GB\n"
            f"Free RAM: {free_ram_gb}GB\n"
            f"Usage: {usage_percentage}%"
        )
    except Exception as e:
        print(f"Failed to get memory information: {e}")

    if not memory_info:
        memory_info = "No memory was found"

    return memory_info


def cpuInfo():
    cpu_info = ""

    try:
        cpu_percentages = psutil.cpu_percent(percpu=True)

        total_cpu_percentage = psutil.cpu_percent()

        core_info = "\n".join(
            [f"Core {i + 1}: {percent}%" for i, percent in enumerate(cpu_percentages)]
        )

        cpu_info = (
            f"Total CPU Usage: {total_cpu_percentage}%\n"
            f"Individual Core Usage:\n{core_info}"
        )
    except Exception as e:
        print(f"Failed to get CPU information: {e}")

    if not cpu_info:
        cpu_info = "No cpu was found"

    return cpu_info


def showRoutines():
    thread_list = ""

    for thread_id, name in threadMonitor.threads["threadsName"].items():
        thread_list += f"- {name}\n"

    if not thread_list:
        thread_list = "No threads were found"

    return thread_list


commandCall = {
    "help": help,
    "diskInfo": diskInfo,
    "memoryInfo": memoryInfo,
    "cpuInfo": cpuInfo,
    "showRoutines": showRoutines,
}
