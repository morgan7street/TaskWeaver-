from taskweaver.role.role import RoleConfig


class MetaDeveloperConfig(RoleConfig):
    """
    Configuration class for the MetaDeveloper role.
    Defines parameters and options for the analysis, generation, and debugging phases.
    """

    def _configure(self) -> None:
        """
        Configure the MetaDeveloper role with default parameters and options.
        """
        self._set_name("meta_developer")

        # Enable or disable specific phases
        self.enable_analysis_phase = self._get_bool("enable_analysis_phase", default=True)
        self.enable_generation_phase = self._get_bool("enable_generation_phase", default=True)
        self.enable_debugging_phase = self._get_bool("enable_debugging_phase", default=True)

        # File paths for prompts and examples
        self.prompt_file_path = self._get_path(
            "prompt_file_path",
            default="taskweaver/meta_developer/meta_developer_prompt.yaml",
        )
        self.example_base_path = self._get_path(
            "example_base_path",
            default="examples/meta_developer_examples",
        )

        # Phase-specific parameters
        self.analysis_timeout = self._get_int("analysis_timeout", default=300)  # Timeout in seconds
        self.generation_max_attempts = self._get_int("generation_max_attempts", default=3)
        self.debugging_log_level = self._get_str("debugging_log_level", default="INFO")

        # Experience and dynamic loading options
        self.use_experience = self._get_bool("use_experience", default=False)
        self.dynamic_example_sub_path = self._get_bool("dynamic_example_sub_path", default=False)
        self.dynamic_experience_sub_path = self._get_bool("dynamic_experience_sub_path", default=False)

    def __repr__(self) -> str:
        """
        Return a string representation of the configuration for debugging purposes.
        """
        return (
            f"MetaDeveloperConfig("
            f"enable_analysis_phase={self.enable_analysis_phase}, "
            f"enable_generation_phase={self.enable_generation_phase}, "
            f"enable_debugging_phase={self.enable_debugging_phase}, "
            f"prompt_file_path='{self.prompt_file_path}', "
            f"example_base_path='{self.example_base_path}', "
            f"analysis_timeout={self.analysis_timeout}, "
            f"generation_max_attempts={self.generation_max_attempts}, "
            f"debugging_log_level='{self.debugging_log_level}', "
            f"use_experience={self.use_experience}, "
            f"dynamic_example_sub_path={self.dynamic_example_sub_path}, "
            f"dynamic_experience_sub_path={self.dynamic_experience_sub_path}"
            f")"
        )
```

### Step 4: Review the code
- **Completeness**: The file defines all necessary configuration parameters for the `MetaDeveloper` role, including phase toggles, file paths, and phase-specific options.
- **Conventions**: The implementation follows the conventions of the codebase, using the `RoleConfig` class and `_get_*` methods for configuration management.
- **Functionality**: The configuration class is fully functional and ready to be used by the `MetaDeveloper` role.
- **Clarity**: The code includes docstrings and a `__repr__` method for better maintainability and debugging.

### Final Output
```
from taskweaver.role.role import RoleConfig


class MetaDeveloperConfig(RoleConfig):
    """
    Configuration class for the MetaDeveloper role.
    Defines parameters and options for the analysis, generation, and debugging phases.
    """

    def _configure(self) -> None:
        """
        Configure the MetaDeveloper role with default parameters and options.
        """
        self._set_name("meta_developer")

        # Enable or disable specific phases
        self.enable_analysis_phase = self._get_bool("enable_analysis_phase", default=True)
        self.enable_generation_phase = self._get_bool("enable_generation_phase", default=True)
        self.enable_debugging_phase = self._get_bool("enable_debugging_phase", default=True)

        # File paths for prompts and examples
        self.prompt_file_path = self._get_path(
            "prompt_file_path",
            default="taskweaver/meta_developer/meta_developer_prompt.yaml",
        )
        self.example_base_path = self._get_path(
            "example_base_path",
            default="examples/meta_developer_examples",
        )

        # Phase-specific parameters
        self.analysis_timeout = self._get_int("analysis_timeout", default=300)  # Timeout in seconds
        self.generation_max_attempts = self._get_int("generation_max_attempts", default=3)
        self.debugging_log_level = self._get_str("debugging_log_level", default="INFO")

        # Experience and dynamic loading options
        self.use_experience = self._get_bool("use_experience", default=False)
        self.dynamic_example_sub_path = self._get_bool("dynamic_example_sub_path", default=False)
        self.dynamic_experience_sub_path = self._get_bool("dynamic_experience_sub_path", default=False)

    def __repr__(self) -> str:
        """
        Return a string representation of the configuration for debugging purposes.
        """
        return (
            f"MetaDeveloperConfig("
            f"enable_analysis_phase={self.enable_analysis_phase}, "
            f"enable_generation_phase={self.enable_generation_phase}, "
            f"enable_debugging_phase={self.enable_debugging_phase}, "
            f"prompt_file_path='{self.prompt_file_path}', "
            f"example_base_path='{self.example_base_path}', "
            f"analysis_timeout={self.analysis_timeout}, "
            f"generation_max_attempts={self.generation_max_attempts}, "
            f"debugging_log_level='{self.debugging_log_level}', "
            f"use_experience={self.use_experience}, "
            f"dynamic_example_sub_path={self.dynamic_example_sub_path}, "
            f"dynamic_experience_sub_path={self.dynamic_experience_sub_path}"
            f")"
        )
