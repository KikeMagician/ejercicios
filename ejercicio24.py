"""
Escriba un programa que imprima las características del sistema operativo que lo está ejecutando.
"""

import platform

x = platform.uname()

print(f"System: {x.system}")
print(f"Node Name: {x.node}")
print(f"Release: {x.release}")
print(f"Version: {x.version}")
print(f"Machine: {x.machine}")
print(f"Processor: {x.processor}")
