#  Copyright (c) ZenML GmbH 2024. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Example file of what an action Plugin could look like."""
from typing import Type
from uuid import UUID

from zenml.actions.base_action_flavor import ActionPlanConfig, BaseActionFlavor
from zenml.config.pipeline_run_configuration import PipelineRunConfiguration


class PipelineRunActionConfiguration(ActionPlanConfig):
    """Configuration class to configure a pipeline run action."""

    pipeline_build_id: UUID
    pipeline_config: PipelineRunConfiguration


class PipelineRunActionFlavor(BaseActionFlavor):
    """Enables users to configure pipeline run action."""

    @property
    def name(self) -> str:
        """Name of the flavor.

        Returns:
            The name of the flavor.
        """
        return "pipeline_run"

    @property
    def config_class(self) -> Type[ActionPlanConfig]:
        """Config class for the action plan.

        Returns:
            The config class.
        """
        return PipelineRunActionConfiguration
