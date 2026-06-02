# Description
SmartLiving Inc. requires a centralized smart home control system that can manage both modern smart devices and legacy systems. The system must maintain a single control point for all devices, support real-time status updates, and ensure consistent state management across the entire network of connected devices. The initial implementation should support smart lights, thermostats, and security systems through a command-line interface.

The system must be designed to prevent control conflicts through centralized management (necessitating a Singleton pattern), support dynamic device registration with real-time updates to all connected devices (requiring an Observer pattern), and seamlessly integrate existing legacy security systems without requiring their replacement (calling for an Adapter pattern).

The solution must be scalable to support up to 50 devices, maintain consistent performance, and be designed in a modular fashion to allow for future enhancements such as GUI implementation, remote access, and mobile app integration. The system should be implemented in Python 3.7 or higher and be capable of running on both Windows and Linux operating systems.
