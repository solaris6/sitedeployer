from pathlib import Path
from typing import Type, List

from sitedeployer.projects.core.Project import Project, logger

class fw_Project(
    Project
):
    def NAME(self) -> str:
        return 'fw'
    
    def pythonanywhere_username(self) -> str:
        return 'getfw'

    def github_url_type(self) -> str:
        return 'ssh'

    def dependencies_lib_temp_Types(self) -> List[Type[Project]]:
        from sitedeployer.projects.builtin.project.base_Project import base_Project
        from sitedeployer.projects.builtin.project.projekt_Project import projekt_Project
        from sitedeployer.projects.builtin.project.myrta_Project import myrta_Project
        return [
            base_Project,
            projekt_Project,
            myrta_Project
        ]

    def dependencies_lib_deployer_Types(self) -> List[Type[Project]]:
        from sitedeployer.projects.builtin.project.base_Project import base_Project
        from sitedeployer.projects.builtin.project.projekt_Project import projekt_Project
        from sitedeployer.projects.builtin.project.myrta_Project import myrta_Project
        from sitedeployer.projects.builtin.project.una_Project import una_Project
        return [
            base_Project,
            projekt_Project,
            myrta_Project,
            una_Project
        ]

    def dependencies_lib_site_Types(self) -> List[Type[Project]]:
        from sitedeployer.projects.builtin.project.base_Project import base_Project
        from sitedeployer.projects.builtin.project.projekt_Project import projekt_Project
        from sitedeployer.projects.builtin.project.una_Project import una_Project
        return [
            base_Project,
            projekt_Project,
            una_Project,
            fw_Project
        ]