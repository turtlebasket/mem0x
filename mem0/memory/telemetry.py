# Telemetry disabled to prevent memory and thread leaks
# All telemetry functions are now no-op stubs


class AnonymousTelemetry:
    """Stub telemetry class that does nothing to prevent resource leaks."""
    
    def __init__(self, vector_store=None):
        pass
    
    def capture_event(self, event_name, properties=None, user_email=None):
        pass
    
    def close(self):
        pass


client_telemetry = AnonymousTelemetry()


def capture_event(event_name, memory_instance, additional_data=None):
    """No-op telemetry function to prevent resource leaks."""
    pass


def capture_client_event(event_name, instance, additional_data=None):
    """No-op telemetry function to prevent resource leaks."""
    pass
