# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .auth_settings import AuthSettings
from .evaluation_settings import EvaluationSettings
from .widget_config import WidgetConfig
from .literal_json_schema_property import LiteralJsonSchemaProperty
from .conversation_initiation_client_data_config import ConversationInitiationClientDataConfig
from .agent_call_limits import AgentCallLimits
from .agent_ban import AgentBan
from .safety import Safety
from .privacy_config import PrivacyConfig
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AgentPlatformSettings(UncheckedBaseModel):
    auth: typing.Optional[AuthSettings] = None
    evaluation: typing.Optional[EvaluationSettings] = None
    widget: typing.Optional[WidgetConfig] = None
    data_collection: typing.Optional[typing.Dict[str, LiteralJsonSchemaProperty]] = None
    overrides: typing.Optional[ConversationInitiationClientDataConfig] = None
    call_limits: typing.Optional[AgentCallLimits] = None
    ban: typing.Optional[AgentBan] = None
    safety: typing.Optional[Safety] = None
    privacy: typing.Optional[PrivacyConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
