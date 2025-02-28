from taskweaver.logging import TelemetryLogger
from taskweaver.module.tracing import tracing_decorator


class DebuggingPhase:
    """
    The DebuggingPhase is responsible for creating custom debugging tools tailored to the generated application.
    It ensures that developers can efficiently identify and resolve issues in the generated code.
    """

    def __init__(self, logger: TelemetryLogger):
        """
        Initialize the DebuggingPhase with a telemetry logger.

        Args:
            logger (TelemetryLogger): Logger for telemetry and debugging information.
        """
        self.logger = logger

    @tracing_decorator
    def run(self, generation_results: dict) -> dict:
        """
        Execute the debugging phase.

        Args:
            generation_results (dict): Results from the generation phase, including generated code and artifacts.

        Returns:
            dict: Custom debugging tools and insights.
        """
        self.logger.info("Starting the debugging phase...")

        # Validate input data
        if not generation_results or "generated_code" not in generation_results:
            self.logger.error("Invalid generation results provided.")
            return {"status": "failure", "error": "Invalid generation results."}

        self.logger.debug(f"Generation results received: {generation_results}")

        # Simulate debugging tool creation logic
        try:
            debugging_tools = self._create_debugging_tools(generation_results["generated_code"])
            self.logger.info("Debugging phase completed successfully.")
            return {"status": "success", "debugging_tools": debugging_tools}
        except Exception as e:
            self.logger.error(f"Error during debugging phase: {str(e)}")
            return {"status": "failure", "error": str(e)}

    def _create_debugging_tools(self, generated_code: dict) -> dict:
        """
        Create debugging tools based on the provided generated code.

        Args:
            generated_code (dict): The generated application code and related artifacts.

        Returns:
            dict: Custom debugging tools and insights.
        """
        self.logger.debug("Creating debugging tools for the generated code...")

        # Placeholder for actual debugging tool creation logic
        # Example: Generate a logging wrapper for each function in the generated code
        debugging_tools = {
            "log_wrappers": [
                f"def log_wrapper(func):\\n"
                f"    def wrapper(*args, **kwargs):\\n"
                f"        print(f'Calling {{func.__name__}} with args={{args}} kwargs={{kwargs}}')\\n"
                f"        result = func(*args, **kwargs)\\n"
                f"        print(f'{{func.__name__}} returned {{result}}')\\n"
                f"        return result\\n"
                f"    return wrapper\\n"
            ],
            "debug_scripts": [
                "import pdb; pdb.set_trace()  # Add this line to set a breakpoint in your code."
            ],
        }

        self.logger.debug(f"Generated debugging tools: {debugging_tools}")
        return debugging_tools
