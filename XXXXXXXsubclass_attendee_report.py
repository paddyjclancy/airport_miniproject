# from class_flights import *
#
#
# class AttendeeReport(Flight):
#
#     def __init__(self, flight, departure, manifest=None):
#         super().__init__(flight, departure)
#         self.manifest = manifest
#         if manifest is None:
#             self.manifest = []
#
#     def append_manifest(self, passenger):
#         self.manifest.append(passenger)
#
#     def full_manifest(self):
#         print(f"\nManifest for personnel on flight {self.flight}: ")
#         for person in self.manifest:
#             print(vars(person))
