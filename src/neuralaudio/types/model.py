# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .language_response import LanguageResponse
from .model_rates_response_model import ModelRatesResponseModel
from .model_response_model_concurrency_group import ModelResponseModelConcurrencyGroup
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Model(UncheckedBaseModel):
    model_id: str
    name: typing.Optional[str] = None
    can_be_finetuned: typing.Optional[bool] = None
    can_do_text_to_speech: typing.Optional[bool] = None
    can_do_voice_conversion: typing.Optional[bool] = None
    can_use_style: typing.Optional[bool] = None
    can_use_speaker_boost: typing.Optional[bool] = None
    serves_pro_voices: typing.Optional[bool] = None
    token_cost_factor: typing.Optional[float] = None
    description: typing.Optional[str] = None
    requires_alpha_access: typing.Optional[bool] = None
    max_characters_request_free_user: typing.Optional[int] = None
    max_characters_request_subscribed_user: typing.Optional[int] = None
    maximum_text_length_per_request: typing.Optional[int] = None
    languages: typing.Optional[typing.List[LanguageResponse]] = None
    model_rates: typing.Optional[ModelRatesResponseModel] = None
    concurrency_group: typing.Optional[ModelResponseModelConcurrencyGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
