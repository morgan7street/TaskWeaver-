from taskweaver.role import RoleRegistry
from .meta_developer import MetaDeveloper

# Register the MetaDeveloper role with TaskWeaver
RoleRegistry.register_role("meta_developer", MetaDeveloper)
