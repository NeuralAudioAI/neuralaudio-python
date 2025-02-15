# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .. import core
from ..core.request_options import RequestOptions
from ..types.do_dubbing_response import DoDubbingResponse
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.dubbing_metadata_response import DubbingMetadataResponse
from ..core.jsonable_encoder import jsonable_encoder
from .types.dubbing_get_transcript_for_dub_request_format_type import DubbingGetTranscriptForDubRequestFormatType
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DubbingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def dub_a_video_or_an_audio_file(
        self,
        *,
        target_lang: str,
        file: typing.Optional[core.File] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_url: typing.Optional[str] = OMIT,
        source_lang: typing.Optional[str] = OMIT,
        num_speakers: typing.Optional[int] = OMIT,
        watermark: typing.Optional[bool] = OMIT,
        start_time: typing.Optional[int] = OMIT,
        end_time: typing.Optional[int] = OMIT,
        highest_resolution: typing.Optional[bool] = OMIT,
        drop_background_audio: typing.Optional[bool] = OMIT,
        use_profanity_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DoDubbingResponse:
        """
        Dubs provided audio or video file into given language.

        Parameters
        ----------
        target_lang : str
            The Target language to dub the content into.

        file : typing.Optional[core.File]
            See core.File for more documentation

        name : typing.Optional[str]
            Name of the dubbing project.

        source_url : typing.Optional[str]
            URL of the source video/audio file.

        source_lang : typing.Optional[str]
            Source language.

        num_speakers : typing.Optional[int]
            Number of speakers to use for the dubbing. Set to 0 to automatically detect the number of speakers

        watermark : typing.Optional[bool]
            Whether to apply watermark to the output video.

        start_time : typing.Optional[int]
            Start time of the source video/audio file.

        end_time : typing.Optional[int]
            End time of the source video/audio file.

        highest_resolution : typing.Optional[bool]
            Whether to use the highest resolution available.

        drop_background_audio : typing.Optional[bool]
            An advanced setting. Whether to drop background audio from the final dub. This can improve dub quality where it's known that audio shouldn't have a background track such as for speeches or monologues.

        use_profanity_filter : typing.Optional[bool]
            [BETA] Whether transcripts should have profanities censored with the words '[censored]'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DoDubbingResponse
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.dub_a_video_or_an_audio_file(
            target_lang="target_lang",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/dubbing",
            method="POST",
            data={
                "name": name,
                "source_url": source_url,
                "source_lang": source_lang,
                "target_lang": target_lang,
                "num_speakers": num_speakers,
                "watermark": watermark,
                "start_time": start_time,
                "end_time": end_time,
                "highest_resolution": highest_resolution,
                "drop_background_audio": drop_background_audio,
                "use_profanity_filter": use_profanity_filter,
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
                    DoDubbingResponse,
                    construct_type(
                        type_=DoDubbingResponse,  # type: ignore
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

    def get_dubbing_project_metadata(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DubbingMetadataResponse:
        """
        Returns metadata about a dubbing project, including whether it's still in progress or not

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingMetadataResponse
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.get_dubbing_project_metadata(
            dubbing_id="dubbing_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DubbingMetadataResponse,
                    construct_type(
                        type_=DubbingMetadataResponse,  # type: ignore
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

    def delete_dubbing_project(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Deletes a dubbing project.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.delete_dubbing_project(
            dubbing_id="dubbing_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
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

    def get_dubbed_file(
        self, dubbing_id: str, language_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns dubbed file as a streamed file. Videos will be returned in MP4 format and audio only dubs will be returned in MP3.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ID of the language.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.Iterator[bytes]
            Successful Response
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}/audio/{jsonable_encoder(language_code)}",
            method="GET",
            request_options=request_options,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    for _chunk in _response.iter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                _response.read()
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

    def get_transcript_for_dub(
        self,
        dubbing_id: str,
        language_code: str,
        *,
        format_type: typing.Optional[DubbingGetTranscriptForDubRequestFormatType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Returns transcript for the dub as an SRT file.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ID of the language.

        format_type : typing.Optional[DubbingGetTranscriptForDubRequestFormatType]
            Format to use for the subtitle file, either 'srt' or 'webvtt'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from neuralaudio import NeuralAudio

        client = NeuralAudio(
            api_key="YOUR_API_KEY",
        )
        client.dubbing.get_transcript_for_dub(
            dubbing_id="dubbing_id",
            language_code="language_code",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}/transcript/{jsonable_encoder(language_code)}",
            method="GET",
            params={
                "format_type": format_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
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


class AsyncDubbingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def dub_a_video_or_an_audio_file(
        self,
        *,
        target_lang: str,
        file: typing.Optional[core.File] = OMIT,
        name: typing.Optional[str] = OMIT,
        source_url: typing.Optional[str] = OMIT,
        source_lang: typing.Optional[str] = OMIT,
        num_speakers: typing.Optional[int] = OMIT,
        watermark: typing.Optional[bool] = OMIT,
        start_time: typing.Optional[int] = OMIT,
        end_time: typing.Optional[int] = OMIT,
        highest_resolution: typing.Optional[bool] = OMIT,
        drop_background_audio: typing.Optional[bool] = OMIT,
        use_profanity_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DoDubbingResponse:
        """
        Dubs provided audio or video file into given language.

        Parameters
        ----------
        target_lang : str
            The Target language to dub the content into.

        file : typing.Optional[core.File]
            See core.File for more documentation

        name : typing.Optional[str]
            Name of the dubbing project.

        source_url : typing.Optional[str]
            URL of the source video/audio file.

        source_lang : typing.Optional[str]
            Source language.

        num_speakers : typing.Optional[int]
            Number of speakers to use for the dubbing. Set to 0 to automatically detect the number of speakers

        watermark : typing.Optional[bool]
            Whether to apply watermark to the output video.

        start_time : typing.Optional[int]
            Start time of the source video/audio file.

        end_time : typing.Optional[int]
            End time of the source video/audio file.

        highest_resolution : typing.Optional[bool]
            Whether to use the highest resolution available.

        drop_background_audio : typing.Optional[bool]
            An advanced setting. Whether to drop background audio from the final dub. This can improve dub quality where it's known that audio shouldn't have a background track such as for speeches or monologues.

        use_profanity_filter : typing.Optional[bool]
            [BETA] Whether transcripts should have profanities censored with the words '[censored]'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DoDubbingResponse
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dubbing.dub_a_video_or_an_audio_file(
                target_lang="target_lang",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/dubbing",
            method="POST",
            data={
                "name": name,
                "source_url": source_url,
                "source_lang": source_lang,
                "target_lang": target_lang,
                "num_speakers": num_speakers,
                "watermark": watermark,
                "start_time": start_time,
                "end_time": end_time,
                "highest_resolution": highest_resolution,
                "drop_background_audio": drop_background_audio,
                "use_profanity_filter": use_profanity_filter,
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
                    DoDubbingResponse,
                    construct_type(
                        type_=DoDubbingResponse,  # type: ignore
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

    async def get_dubbing_project_metadata(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DubbingMetadataResponse:
        """
        Returns metadata about a dubbing project, including whether it's still in progress or not

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingMetadataResponse
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dubbing.get_dubbing_project_metadata(
                dubbing_id="dubbing_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DubbingMetadataResponse,
                    construct_type(
                        type_=DubbingMetadataResponse,  # type: ignore
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

    async def delete_dubbing_project(
        self, dubbing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Deletes a dubbing project.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dubbing.delete_dubbing_project(
                dubbing_id="dubbing_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
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

    async def get_dubbed_file(
        self, dubbing_id: str, language_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns dubbed file as a streamed file. Videos will be returned in MP4 format and audio only dubs will be returned in MP3.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ID of the language.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.AsyncIterator[bytes]
            Successful Response
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}/audio/{jsonable_encoder(language_code)}",
            method="GET",
            request_options=request_options,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                await _response.aread()
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

    async def get_transcript_for_dub(
        self,
        dubbing_id: str,
        language_code: str,
        *,
        format_type: typing.Optional[DubbingGetTranscriptForDubRequestFormatType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Returns transcript for the dub as an SRT file.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language_code : str
            ID of the language.

        format_type : typing.Optional[DubbingGetTranscriptForDubRequestFormatType]
            Format to use for the subtitle file, either 'srt' or 'webvtt'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from neuralaudio import AsyncNeuralAudio

        client = AsyncNeuralAudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dubbing.get_transcript_for_dub(
                dubbing_id="dubbing_id",
                language_code="language_code",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dubbing/{jsonable_encoder(dubbing_id)}/transcript/{jsonable_encoder(language_code)}",
            method="GET",
            params={
                "format_type": format_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
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
