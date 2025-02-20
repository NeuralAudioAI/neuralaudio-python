# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .. import core
from .types.pronunciation_dictionary_add_from_file_request_workspace_access import (
    PronunciationDictionaryAddFromFileRequestWorkspaceAccess,
)
from ..core.request_options import RequestOptions
from ..types.add_pronunciation_dictionary_response_model import AddPronunciationDictionaryResponseModel
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.pronunciation_dictionary_rule import PronunciationDictionaryRule
from ..types.add_pronunciation_dictionary_rules_response_model import AddPronunciationDictionaryRulesResponseModel
from ..core.jsonable_encoder import jsonable_encoder
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.remove_pronunciation_dictionary_rules_response_model import RemovePronunciationDictionaryRulesResponseModel
from ..types.get_pronunciation_dictionary_metadata_response import GetPronunciationDictionaryMetadataResponse
from ..types.get_pronunciation_dictionaries_metadata_response_model import (
    GetPronunciationDictionariesMetadataResponseModel,
)
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PronunciationDictionaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_from_file(
        self,
        *,
        name: str,
        file: typing.Optional[core.File] = OMIT,
        description: typing.Optional[str] = OMIT,
        workspace_access: typing.Optional[PronunciationDictionaryAddFromFileRequestWorkspaceAccess] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddPronunciationDictionaryResponseModel:
        """
        Creates a new pronunciation dictionary from a lexicon .PLS file

        Parameters
        ----------
        name : str
            The name of the pronunciation dictionary, used for identification only.

        file : typing.Optional[core.File]
            See core.File for more documentation

        description : typing.Optional[str]
            A description of the pronunciation dictionary, used for identification only.

        workspace_access : typing.Optional[PronunciationDictionaryAddFromFileRequestWorkspaceAccess]
            Should be one of 'editor' or 'viewer'. If not provided, defaults to no access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.pronunciation_dictionary.add_from_file(
            name="name",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/pronunciation-dictionaries/add-from-file",
            method="POST",
            data={
                "name": name,
                "description": description,
                "workspace_access": workspace_access,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AddPronunciationDictionaryResponseModel,
                    construct_type(
                        type_=AddPronunciationDictionaryResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add_rules(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: typing.Sequence[PronunciationDictionaryRule],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddPronunciationDictionaryRulesResponseModel:
        """
        Add rules to the pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rules : typing.Sequence[PronunciationDictionaryRule]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio
        from neuralaudio.pronunciation_dictionary import (
            PronunciationDictionaryRule_Alias,
        )

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.pronunciation_dictionary.add_rules(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            rules=[
                PronunciationDictionaryRule_Alias(
                    string_to_replace="string_to_replace",
                    alias="alias",
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(pronunciation_dictionary_id)}/add-rules",
            method="POST",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[PronunciationDictionaryRule], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AddPronunciationDictionaryRulesResponseModel,
                    construct_type(
                        type_=AddPronunciationDictionaryRulesResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove_rules(
        self,
        pronunciation_dictionary_id: str,
        *,
        rule_strings: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemovePronunciationDictionaryRulesResponseModel:
        """
        Remove rules from the pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rule_strings : typing.Sequence[str]
            List of strings to remove from the pronunciation dictionary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemovePronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.pronunciation_dictionary.remove_rules(
            pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
            rule_strings=["rule_strings"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(pronunciation_dictionary_id)}/remove-rules",
            method="POST",
            json={
                "rule_strings": rule_strings,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RemovePronunciationDictionaryRulesResponseModel,
                    construct_type(
                        type_=RemovePronunciationDictionaryRulesResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def download(
        self, dictionary_id: str, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get PLS file with a pronunciation dictionary version rules

        Parameters
        ----------
        dictionary_id : str
            The id of the pronunciation dictionary

        version_id : str
            The id of the version of the pronunciation dictionary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.pronunciation_dictionary.download(
            dictionary_id="Fm6AvNgS53NXe6Kqxp3e",
            version_id="KZFyRUq3R6kaqhKI146w",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(dictionary_id)}/{jsonable_encoder(version_id)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return _response.text  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, pronunciation_dictionary_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPronunciationDictionaryMetadataResponse:
        """
        Get metadata for a pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionaryMetadataResponse
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.pronunciation_dictionary.get(
            pronunciation_dictionary_id="Fm6AvNgS53NXe6Kqxp3e",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(pronunciation_dictionary_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GetPronunciationDictionaryMetadataResponse,
                    construct_type(
                        type_=GetPronunciationDictionaryMetadataResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all(
        self,
        *,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPronunciationDictionariesMetadataResponseModel:
        """
        Get a list of the pronunciation dictionaries you have access to and their metadata

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many pronunciation dictionaries to return at maximum. Can not exceed 100, defaults to 30.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionariesMetadataResponseModel
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.pronunciation_dictionary.get_all(
            page_size=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/pronunciation-dictionaries/",
            method="GET",
            params={
                "cursor": cursor,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GetPronunciationDictionariesMetadataResponseModel,
                    construct_type(
                        type_=GetPronunciationDictionariesMetadataResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPronunciationDictionaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_from_file(
        self,
        *,
        name: str,
        file: typing.Optional[core.File] = OMIT,
        description: typing.Optional[str] = OMIT,
        workspace_access: typing.Optional[PronunciationDictionaryAddFromFileRequestWorkspaceAccess] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddPronunciationDictionaryResponseModel:
        """
        Creates a new pronunciation dictionary from a lexicon .PLS file

        Parameters
        ----------
        name : str
            The name of the pronunciation dictionary, used for identification only.

        file : typing.Optional[core.File]
            See core.File for more documentation

        description : typing.Optional[str]
            A description of the pronunciation dictionary, used for identification only.

        workspace_access : typing.Optional[PronunciationDictionaryAddFromFileRequestWorkspaceAccess]
            Should be one of 'editor' or 'viewer'. If not provided, defaults to no access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pronunciation_dictionary.add_from_file(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/pronunciation-dictionaries/add-from-file",
            method="POST",
            data={
                "name": name,
                "description": description,
                "workspace_access": workspace_access,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AddPronunciationDictionaryResponseModel,
                    construct_type(
                        type_=AddPronunciationDictionaryResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add_rules(
        self,
        pronunciation_dictionary_id: str,
        *,
        rules: typing.Sequence[PronunciationDictionaryRule],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddPronunciationDictionaryRulesResponseModel:
        """
        Add rules to the pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rules : typing.Sequence[PronunciationDictionaryRule]
            List of pronunciation rules. Rule can be either:
                an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', }
                or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddPronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio
        from neuralaudio.pronunciation_dictionary import (
            PronunciationDictionaryRule_Alias,
        )

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pronunciation_dictionary.add_rules(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
                rules=[
                    PronunciationDictionaryRule_Alias(
                        string_to_replace="string_to_replace",
                        alias="alias",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(pronunciation_dictionary_id)}/add-rules",
            method="POST",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[PronunciationDictionaryRule], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AddPronunciationDictionaryRulesResponseModel,
                    construct_type(
                        type_=AddPronunciationDictionaryRulesResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove_rules(
        self,
        pronunciation_dictionary_id: str,
        *,
        rule_strings: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemovePronunciationDictionaryRulesResponseModel:
        """
        Remove rules from the pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        rule_strings : typing.Sequence[str]
            List of strings to remove from the pronunciation dictionary.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemovePronunciationDictionaryRulesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pronunciation_dictionary.remove_rules(
                pronunciation_dictionary_id="21m00Tcm4TlvDq8ikWAM",
                rule_strings=["rule_strings"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(pronunciation_dictionary_id)}/remove-rules",
            method="POST",
            json={
                "rule_strings": rule_strings,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RemovePronunciationDictionaryRulesResponseModel,
                    construct_type(
                        type_=RemovePronunciationDictionaryRulesResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def download(
        self, dictionary_id: str, version_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Get PLS file with a pronunciation dictionary version rules

        Parameters
        ----------
        dictionary_id : str
            The id of the pronunciation dictionary

        version_id : str
            The id of the version of the pronunciation dictionary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pronunciation_dictionary.download(
                dictionary_id="Fm6AvNgS53NXe6Kqxp3e",
                version_id="KZFyRUq3R6kaqhKI146w",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(dictionary_id)}/{jsonable_encoder(version_id)}/download",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return _response.text  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, pronunciation_dictionary_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPronunciationDictionaryMetadataResponse:
        """
        Get metadata for a pronunciation dictionary

        Parameters
        ----------
        pronunciation_dictionary_id : str
            The id of the pronunciation dictionary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionaryMetadataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pronunciation_dictionary.get(
                pronunciation_dictionary_id="Fm6AvNgS53NXe6Kqxp3e",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pronunciation-dictionaries/{jsonable_encoder(pronunciation_dictionary_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GetPronunciationDictionaryMetadataResponse,
                    construct_type(
                        type_=GetPronunciationDictionaryMetadataResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all(
        self,
        *,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetPronunciationDictionariesMetadataResponseModel:
        """
        Get a list of the pronunciation dictionaries you have access to and their metadata

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many pronunciation dictionaries to return at maximum. Can not exceed 100, defaults to 30.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPronunciationDictionariesMetadataResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pronunciation_dictionary.get_all(
                page_size=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/pronunciation-dictionaries/",
            method="GET",
            params={
                "cursor": cursor,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GetPronunciationDictionariesMetadataResponseModel,
                    construct_type(
                        type_=GetPronunciationDictionariesMetadataResponseModel,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
