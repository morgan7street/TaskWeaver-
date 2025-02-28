# MetaDeveloper README

## Overview

The `MetaDeveloper` is a core component of the TaskWeaver framework, designed to streamline and automate the software development process. It achieves this by orchestrating three key phases: **Analysis**, **Generation**, and **Debugging**. These phases work together to analyze existing codebases, generate new application code, and create custom debugging tools. The `MetaDeveloper` integrates seamlessly with TaskWeaver, leveraging its planning and execution capabilities to deliver a cohesive development experience.

---

## Architecture

The `MetaDeveloper` is structured into the following components:

1. **Analysis Phase**:
   - Responsible for analyzing the structure and content of the codebase.
   - Generates tools and insights to facilitate deeper understanding of the project.
   - Outputs data that informs the subsequent phases.

2. **Generation Phase**:
   - Uses the results of the analysis phase to generate new application code.
   - Ensures that the generated code aligns with the project's architecture and requirements.

3. **Debugging Phase**:
   - Creates custom debugging tools tailored to the generated application.
   - Helps identify and resolve issues efficiently.

4. **Configuration**:
   - Centralized configuration file (`config.py`) to define parameters and options for the `MetaDeveloper`.

5. **Attachment Types**:
   - Defines specific attachment types (`attachment_type.py`) used across the phases to standardize communication and data exchange.

6. **Prompt Definitions**:
   - A YAML-based prompt file (`meta_developer_prompt.yaml`) that specifies instructions and expected response formats for the `MetaDeveloper`.

7. **Examples**:
   - Includes example workflows (`examples/meta_developer_examples`) to demonstrate how to use the `MetaDeveloper` effectively.

---

## Integration with TaskWeaver

The `MetaDeveloper` is registered as a role within TaskWeaver, enabling it to collaborate with other roles like the Planner and CodeInterpreter. This integration allows the `MetaDeveloper` to:

- Receive high-level tasks from the Planner.
- Execute its three phases in a structured manner.
- Provide results and feedback to the Planner for further action.

The `MetaDeveloper` relies on TaskWeaver's robust planning and execution framework to ensure that its operations are efficient and aligned with the overall project goals.

---

## Usage

To use the `MetaDeveloper`, follow these steps:

1. **Initialization**:
   - Ensure that the `MetaDeveloper` is registered with TaskWeaver by including the `__init__.py` file in the `meta_developer` module.

2. **Configuration**:
   - Customize the `config.py` file to define the parameters for the analysis, generation, and debugging phases.

3. **Execution**:
   - Use the Planner to assign tasks to the `MetaDeveloper`.
   - Monitor the progress of each phase through TaskWeaver's logging and reporting mechanisms.

4. **Examples**:
   - Refer to the example workflows in the `examples/meta_developer_examples` directory for guidance on how to use the `MetaDeveloper` in real-world scenarios.

---

## File Structure

The `MetaDeveloper` module is organized as follows:

```
taskweaver/meta_developer/
├── README.md                # Documentation for the MetaDeveloper
├── __init__.py              # Module initialization and role registration
├── meta_developer.py        # Main orchestrator for the three phases
├── analysis_phase.py        # Implementation of the analysis phase
├── generation_phase.py      # Implementation of the generation phase
├── debugging_phase.py       # Implementation of the debugging phase
├── config.py                # Configuration file for the MetaDeveloper
├── attachment_type.py       # Definitions of attachment types
├── meta_developer_prompt.yaml # Prompt definitions for the MetaDeveloper
```

---

## Example Workflow

An example workflow for the `MetaDeveloper` might look like this:

1. **Task Assignment**:
   - The Planner assigns a task to the `MetaDeveloper` to analyze a codebase and generate new features.

2. **Analysis Phase**:
   - The `MetaDeveloper` analyzes the codebase and outputs insights.

3. **Generation Phase**:
   - Based on the analysis, the `MetaDeveloper` generates new application code.

4. **Debugging Phase**:
   - Custom debugging tools are created to test and refine the generated code.

5. **Feedback**:
   - The results are sent back to the Planner for review and further action.

---

By leveraging the `MetaDeveloper`, TaskWeaver users can automate and enhance their software development workflows, reducing manual effort and improving efficiency.
