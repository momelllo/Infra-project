import logging
from datetime import datetime

class Machine:
    def __init__(self, name, os, cpu, ram, storage):
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        logging.info(f"Machine created: {self.name} ({self.os}, CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB)")

    def to_dict(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram,
            "storage": self.storage,
        }