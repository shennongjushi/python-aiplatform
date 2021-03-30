# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.aiplatform_v1beta1.types import artifact as gca_artifact
from google.cloud.aiplatform_v1beta1.types import context as gca_context
from google.cloud.aiplatform_v1beta1.types import event
from google.cloud.aiplatform_v1beta1.types import execution as gca_execution
from google.cloud.aiplatform_v1beta1.types import metadata_schema as gca_metadata_schema
from google.cloud.aiplatform_v1beta1.types import metadata_store as gca_metadata_store
from google.cloud.aiplatform_v1beta1.types import operation
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.aiplatform.v1beta1',
    manifest={
        'CreateMetadataStoreRequest',
        'CreateMetadataStoreOperationMetadata',
        'GetMetadataStoreRequest',
        'ListMetadataStoresRequest',
        'ListMetadataStoresResponse',
        'DeleteMetadataStoreRequest',
        'DeleteMetadataStoreOperationMetadata',
        'CreateArtifactRequest',
        'GetArtifactRequest',
        'ListArtifactsRequest',
        'ListArtifactsResponse',
        'UpdateArtifactRequest',
        'CreateContextRequest',
        'GetContextRequest',
        'ListContextsRequest',
        'ListContextsResponse',
        'UpdateContextRequest',
        'DeleteContextRequest',
        'AddContextArtifactsAndExecutionsRequest',
        'AddContextArtifactsAndExecutionsResponse',
        'AddContextChildrenRequest',
        'AddContextChildrenResponse',
        'QueryContextLineageSubgraphRequest',
        'CreateExecutionRequest',
        'GetExecutionRequest',
        'ListExecutionsRequest',
        'ListExecutionsResponse',
        'UpdateExecutionRequest',
        'AddExecutionEventsRequest',
        'AddExecutionEventsResponse',
        'QueryExecutionInputsAndOutputsRequest',
        'CreateMetadataSchemaRequest',
        'GetMetadataSchemaRequest',
        'ListMetadataSchemasRequest',
        'ListMetadataSchemasResponse',
    },
)


class CreateMetadataStoreRequest(proto.Message):
    r"""Request message for
    ``MetadataService.CreateMetadataStore``.

    Attributes:
        parent (str):
            Required. The resource name of the Location
            where the MetadataStore should be created.
            Format: projects/{project}/locations/{location}/
        metadata_store (google.cloud.aiplatform_v1beta1.types.MetadataStore):
            Required. The MetadataStore to create.
        metadata_store_id (str):
            The {metadatastore} portion of the resource name with the
            format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
            If not provided, the MetadataStore's ID will be a UUID
            generated by the service. Must be 4-128 characters in
            length. Valid characters are /[a-z][0-9]-/. Must be unique
            across all MetadataStores in the parent Location. (Otherwise
            the request will fail with ALREADY_EXISTS, or
            PERMISSION_DENIED if the caller can't view the preexisting
            MetadataStore.)
    """

    parent = proto.Field(proto.STRING, number=1)

    metadata_store = proto.Field(proto.MESSAGE, number=2,
        message=gca_metadata_store.MetadataStore,
    )

    metadata_store_id = proto.Field(proto.STRING, number=3)


class CreateMetadataStoreOperationMetadata(proto.Message):
    r"""Details of operations that perform
    ``MetadataService.CreateMetadataStore``.

    Attributes:
        generic_metadata (google.cloud.aiplatform_v1beta1.types.GenericOperationMetadata):
            Operation metadata for creating a
            MetadataStore.
    """

    generic_metadata = proto.Field(proto.MESSAGE, number=1,
        message=operation.GenericOperationMetadata,
    )


class GetMetadataStoreRequest(proto.Message):
    r"""Request message for
    ``MetadataService.GetMetadataStore``.

    Attributes:
        name (str):
            Required. The resource name of the
            MetadataStore to retrieve. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
    """

    name = proto.Field(proto.STRING, number=1)


class ListMetadataStoresRequest(proto.Message):
    r"""Request message for
    ``MetadataService.ListMetadataStores``.

    Attributes:
        parent (str):
            Required. The Location whose MetadataStores
            should be listed. Format:
            projects/{project}/locations/{location}
        page_size (int):
            The maximum number of Metadata Stores to
            return. The service may return fewer.
            Must be in range 1-1000, inclusive. Defaults to
            100.
        page_token (str):
            A page token, received from a previous
            ``MetadataService.ListMetadataStores``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other provided parameters must match
            the call that provided the page token. (Otherwise the
            request will fail with INVALID_ARGUMENT error.)
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)


class ListMetadataStoresResponse(proto.Message):
    r"""Response message for
    ``MetadataService.ListMetadataStores``.

    Attributes:
        metadata_stores (Sequence[google.cloud.aiplatform_v1beta1.types.MetadataStore]):
            The MetadataStores found for the Location.
        next_page_token (str):
            A token, which can be sent as
            [MetadataService.ListMetadataStores.page_token][] to
            retrieve the next page. If this field is not populated,
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    metadata_stores = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gca_metadata_store.MetadataStore,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteMetadataStoreRequest(proto.Message):
    r"""Request message for
    ``MetadataService.DeleteMetadataStore``.

    Attributes:
        name (str):
            Required. The resource name of the
            MetadataStore to delete. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        force (bool):
            If set to true, any child resources of this MetadataStore
            will be deleted. (Otherwise, the request will fail with a
            FAILED_PRECONDITION error if the MetadataStore has any child
            resources.)
    """

    name = proto.Field(proto.STRING, number=1)

    force = proto.Field(proto.BOOL, number=2)


class DeleteMetadataStoreOperationMetadata(proto.Message):
    r"""Details of operations that perform
    ``MetadataService.DeleteMetadataStore``.

    Attributes:
        generic_metadata (google.cloud.aiplatform_v1beta1.types.GenericOperationMetadata):
            Operation metadata for deleting a
            MetadataStore.
    """

    generic_metadata = proto.Field(proto.MESSAGE, number=1,
        message=operation.GenericOperationMetadata,
    )


class CreateArtifactRequest(proto.Message):
    r"""Request message for
    ``MetadataService.CreateArtifact``.

    Attributes:
        parent (str):
            Required. The resource name of the
            MetadataStore where the Artifact should be
            created. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        artifact (google.cloud.aiplatform_v1beta1.types.Artifact):
            Required. The Artifact to create.
        artifact_id (str):
            The {artifact} portion of the resource name with the format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}
            If not provided, the Artifact's ID will be a UUID generated
            by the service. Must be 4-128 characters in length. Valid
            characters are /[a-z][0-9]-/. Must be unique across all
            Artifacts in the parent MetadataStore. (Otherwise the
            request will fail with ALREADY_EXISTS, or PERMISSION_DENIED
            if the caller can't view the preexisting Artifact.)
    """

    parent = proto.Field(proto.STRING, number=1)

    artifact = proto.Field(proto.MESSAGE, number=2,
        message=gca_artifact.Artifact,
    )

    artifact_id = proto.Field(proto.STRING, number=3)


class GetArtifactRequest(proto.Message):
    r"""Request message for
    ``MetadataService.GetArtifact``.

    Attributes:
        name (str):
            Required. The resource name of the Artifact
            to retrieve. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}
    """

    name = proto.Field(proto.STRING, number=1)


class ListArtifactsRequest(proto.Message):
    r"""Request message for
    ``MetadataService.ListArtifacts``.

    Attributes:
        parent (str):
            Required. The MetadataStore whose Artifacts
            should be listed. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        page_size (int):
            The maximum number of Artifacts to return.
            The service may return fewer. Must be in range
            1-1000, inclusive. Defaults to 100.
        page_token (str):
            A page token, received from a previous
            ``MetadataService.ListArtifacts``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other provided parameters must match
            the call that provided the page token. (Otherwise the
            request will fail with INVALID_ARGUMENT error.)
        filter (str):
            A query to filter available Artifacts for
            matching results.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    filter = proto.Field(proto.STRING, number=4)


class ListArtifactsResponse(proto.Message):
    r"""Response message for
    ``MetadataService.ListArtifacts``.

    Attributes:
        artifacts (Sequence[google.cloud.aiplatform_v1beta1.types.Artifact]):
            The Artifacts retrieved from the
            MetadataStore.
        next_page_token (str):
            A token, which can be sent as
            [MetadataService.ListArtifacts.page_token][] to retrieve the
            next page. If this field is not populated, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    artifacts = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gca_artifact.Artifact,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class UpdateArtifactRequest(proto.Message):
    r"""Request message for
    ``MetadataService.UpdateArtifact``.

    Attributes:
        artifact (google.cloud.aiplatform_v1beta1.types.Artifact):
            Required. The Artifact containing updates. The Artifact's
            ``Artifact.name``
            field is used to identify the Artifact to be updated.
            Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A FieldMask indicating which fields
            should be updated.
        allow_missing (bool):
            If set to true, and the
            ``Artifact`` is not
            found, a new
            ``Artifact`` will be
            created. In this situation, ``update_mask`` is ignored.
    """

    artifact = proto.Field(proto.MESSAGE, number=1,
        message=gca_artifact.Artifact,
    )

    update_mask = proto.Field(proto.MESSAGE, number=2,
        message=field_mask.FieldMask,
    )

    allow_missing = proto.Field(proto.BOOL, number=3)


class CreateContextRequest(proto.Message):
    r"""Request message for
    ``MetadataService.CreateContext``.

    Attributes:
        parent (str):
            Required. The resource name of the
            MetadataStore where the Context should be
            created. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        context (google.cloud.aiplatform_v1beta1.types.Context):
            Required. The Context to create.
        context_id (str):
            The {context} portion of the resource name with the format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}
            If not provided, the Context's ID will be a UUID generated
            by the service. Must be 4-128 characters in length. Valid
            characters are /[a-z][0-9]-/. Must be unique across all
            Contexts in the parent MetadataStore. (Otherwise the request
            will fail with ALREADY_EXISTS, or PERMISSION_DENIED if the
            caller can't view the preexisting Context.)
    """

    parent = proto.Field(proto.STRING, number=1)

    context = proto.Field(proto.MESSAGE, number=2,
        message=gca_context.Context,
    )

    context_id = proto.Field(proto.STRING, number=3)


class GetContextRequest(proto.Message):
    r"""Request message for
    ``MetadataService.GetContext``.

    Attributes:
        name (str):
            Required. The resource name of the Context to
            retrieve. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}
    """

    name = proto.Field(proto.STRING, number=1)


class ListContextsRequest(proto.Message):
    r"""Request message for
    ``MetadataService.ListContexts``

    Attributes:
        parent (str):
            Required. The MetadataStore whose Contexts
            should be listed. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        page_size (int):
            The maximum number of Contexts to return. The
            service may return fewer. Must be in range
            1-1000, inclusive. Defaults to 100.
        page_token (str):
            A page token, received from a previous
            ``MetadataService.ListContexts``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other provided parameters must match
            the call that provided the page token. (Otherwise the
            request will fail with INVALID_ARGUMENT error.)
        filter (str):
            A query to filter available Contexts for
            matching results.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    filter = proto.Field(proto.STRING, number=4)


class ListContextsResponse(proto.Message):
    r"""Response message for
    ``MetadataService.ListContexts``.

    Attributes:
        contexts (Sequence[google.cloud.aiplatform_v1beta1.types.Context]):
            The Contexts retrieved from the
            MetadataStore.
        next_page_token (str):
            A token, which can be sent as
            [MetadataService.ListContexts.page_token][] to retrieve the
            next page. If this field is not populated, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    contexts = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gca_context.Context,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class UpdateContextRequest(proto.Message):
    r"""Request message for
    ``MetadataService.UpdateContext``.

    Attributes:
        context (google.cloud.aiplatform_v1beta1.types.Context):
            Required. The Context containing updates. The Context's
            ``Context.name``
            field is used to identify the Context to be updated. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A FieldMask indicating which fields
            should be updated.
        allow_missing (bool):
            If set to true, and the
            ``Context`` is not
            found, a new
            ``Context`` will be
            created. In this situation, ``update_mask`` is ignored.
    """

    context = proto.Field(proto.MESSAGE, number=1,
        message=gca_context.Context,
    )

    update_mask = proto.Field(proto.MESSAGE, number=2,
        message=field_mask.FieldMask,
    )

    allow_missing = proto.Field(proto.BOOL, number=3)


class DeleteContextRequest(proto.Message):
    r"""Request message for
    ``MetadataService.DeleteContext``.

    Attributes:
        name (str):
            Required. The resource name of the Context to
            retrieve. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}
        force (bool):
            If set to true, any child resources of this Context will be
            deleted. (Otherwise, the request will fail with a
            FAILED_PRECONDITION error if the Context has any child
            resources, such as another Context, Artifact, or Execution).
    """

    name = proto.Field(proto.STRING, number=1)

    force = proto.Field(proto.BOOL, number=2)


class AddContextArtifactsAndExecutionsRequest(proto.Message):
    r"""Request message for
    ``MetadataService.AddContextArtifactsAndExecutions``.

    Attributes:
        context (str):
            Required. The resource name of the Context
            that the Artifacts and Executions belong to.
            Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}
        artifacts (Sequence[str]):
            The resource names of the Artifacts to
            attribute to the Context.
        executions (Sequence[str]):
            The resource names of the Executions to
            associate with the Context.
    """

    context = proto.Field(proto.STRING, number=1)

    artifacts = proto.RepeatedField(proto.STRING, number=2)

    executions = proto.RepeatedField(proto.STRING, number=3)


class AddContextArtifactsAndExecutionsResponse(proto.Message):
    r"""Response message for
    ``MetadataService.AddContextArtifactsAndExecutions``.
    """


class AddContextChildrenRequest(proto.Message):
    r"""Request message for
    ``MetadataService.AddContextChildren``.

    Attributes:
        context (str):
            Required. The resource name of the parent
            Context. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}
        child_contexts (Sequence[str]):
            The resource names of the child Contexts.
    """

    context = proto.Field(proto.STRING, number=1)

    child_contexts = proto.RepeatedField(proto.STRING, number=2)


class AddContextChildrenResponse(proto.Message):
    r"""Response message for
    ``MetadataService.AddContextChildren``.
    """


class QueryContextLineageSubgraphRequest(proto.Message):
    r"""Request message for
    ``MetadataService.QueryContextLineageSubgraph``.

    Attributes:
        context (str):
            Required. The resource name of the Context whose Artifacts
            and Executions should be retrieved as a LineageSubgraph.
            Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/contexts/{context}

            The request may error with FAILED_PRECONDITION if the number
            of Artifacts, the number of Executions, or the number of
            Events that would be returned for the Context exceeds 1000.
    """

    context = proto.Field(proto.STRING, number=1)


class CreateExecutionRequest(proto.Message):
    r"""Request message for
    ``MetadataService.CreateExecution``.

    Attributes:
        parent (str):
            Required. The resource name of the
            MetadataStore where the Execution should be
            created. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        execution (google.cloud.aiplatform_v1beta1.types.Execution):
            Required. The Execution to create.
        execution_id (str):
            The {execution} portion of the resource name with the
            format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}
            If not provided, the Execution's ID will be a UUID generated
            by the service. Must be 4-128 characters in length. Valid
            characters are /[a-z][0-9]-/. Must be unique across all
            Executions in the parent MetadataStore. (Otherwise the
            request will fail with ALREADY_EXISTS, or PERMISSION_DENIED
            if the caller can't view the preexisting Execution.)
    """

    parent = proto.Field(proto.STRING, number=1)

    execution = proto.Field(proto.MESSAGE, number=2,
        message=gca_execution.Execution,
    )

    execution_id = proto.Field(proto.STRING, number=3)


class GetExecutionRequest(proto.Message):
    r"""Request message for
    ``MetadataService.GetExecution``.

    Attributes:
        name (str):
            Required. The resource name of the Execution
            to retrieve. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}
    """

    name = proto.Field(proto.STRING, number=1)


class ListExecutionsRequest(proto.Message):
    r"""Request message for
    ``MetadataService.ListExecutions``.

    Attributes:
        parent (str):
            Required. The MetadataStore whose Executions
            should be listed. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        page_size (int):
            The maximum number of Executions to return.
            The service may return fewer. Must be in range
            1-1000, inclusive. Defaults to 100.
        page_token (str):
            A page token, received from a previous
            ``MetadataService.ListExecutions``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other provided parameters must match
            the call that provided the page token. (Otherwise the
            request will fail with INVALID_ARGUMENT error.)
        filter (str):
            A query to filter available Executions for matching results.
            Current implementation supports filtering on fields:

            1) display_name e.g display_name = "test_name"
            2) state e.g. state = RUNNING
            3) create_time and update_time e.g create_time >
               "2020-12-17T13:25:12-08:00"
            4) metadata e.g metadata.flag.number_value > 1
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    filter = proto.Field(proto.STRING, number=4)


class ListExecutionsResponse(proto.Message):
    r"""Response message for
    ``MetadataService.ListExecutions``.

    Attributes:
        executions (Sequence[google.cloud.aiplatform_v1beta1.types.Execution]):
            The Executions retrieved from the
            MetadataStore.
        next_page_token (str):
            A token, which can be sent as
            [MetadataService.ListExecutions.page_token][] to retrieve
            the next page. If this field is not populated, there are no
            subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    executions = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gca_execution.Execution,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class UpdateExecutionRequest(proto.Message):
    r"""Request message for
    ``MetadataService.UpdateExecution``.

    Attributes:
        execution (google.cloud.aiplatform_v1beta1.types.Execution):
            Required. The Execution containing updates. The Execution's
            ``Execution.name``
            field is used to identify the Execution to be updated.
            Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A FieldMask indicating which fields
            should be updated.
        allow_missing (bool):
            If set to true, and the
            ``Execution`` is
            not found, a new
            ``Execution`` will
            be created. In this situation, ``update_mask`` is ignored.
    """

    execution = proto.Field(proto.MESSAGE, number=1,
        message=gca_execution.Execution,
    )

    update_mask = proto.Field(proto.MESSAGE, number=2,
        message=field_mask.FieldMask,
    )

    allow_missing = proto.Field(proto.BOOL, number=3)


class AddExecutionEventsRequest(proto.Message):
    r"""Request message for
    ``MetadataService.AddExecutionEvents``.

    Attributes:
        execution (str):
            Required. The resource name of the Execution
            that the Events connect Artifacts with.
            Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}
        events (Sequence[google.cloud.aiplatform_v1beta1.types.Event]):
            The Events to create and add.
    """

    execution = proto.Field(proto.STRING, number=1)

    events = proto.RepeatedField(proto.MESSAGE, number=2,
        message=event.Event,
    )


class AddExecutionEventsResponse(proto.Message):
    r"""Response message for
    ``MetadataService.AddExecutionEvents``.
    """


class QueryExecutionInputsAndOutputsRequest(proto.Message):
    r"""Request message for
    ``MetadataService.QueryExecutionInputsAndOutputs``.

    Attributes:
        execution (str):
            Required. The resource name of the Execution
            whose input and output Artifacts should be
            retrieved as a LineageSubgraph. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}
    """

    execution = proto.Field(proto.STRING, number=1)


class CreateMetadataSchemaRequest(proto.Message):
    r"""Request message for
    ``MetadataService.CreateMetadataSchema``.

    Attributes:
        parent (str):
            Required. The resource name of the
            MetadataStore where the MetadataSchema should be
            created. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        metadata_schema (google.cloud.aiplatform_v1beta1.types.MetadataSchema):
            Required. The MetadataSchema to create.
        metadata_schema_id (str):
            The {metadata_schema} portion of the resource name with the
            format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}
            If not provided, the MetadataStore's ID will be a UUID
            generated by the service. Must be 4-128 characters in
            length. Valid characters are /[a-z][0-9]-/. Must be unique
            across all MetadataSchemas in the parent Location.
            (Otherwise the request will fail with ALREADY_EXISTS, or
            PERMISSION_DENIED if the caller can't view the preexisting
            MetadataSchema.)
    """

    parent = proto.Field(proto.STRING, number=1)

    metadata_schema = proto.Field(proto.MESSAGE, number=2,
        message=gca_metadata_schema.MetadataSchema,
    )

    metadata_schema_id = proto.Field(proto.STRING, number=3)


class GetMetadataSchemaRequest(proto.Message):
    r"""Request message for
    ``MetadataService.GetMetadataSchema``.

    Attributes:
        name (str):
            Required. The resource name of the
            MetadataSchema to retrieve. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}/metadataSchemas/{metadataschema}
    """

    name = proto.Field(proto.STRING, number=1)


class ListMetadataSchemasRequest(proto.Message):
    r"""Request message for
    ``MetadataService.ListMetadataSchemas``.

    Attributes:
        parent (str):
            Required. The MetadataStore whose
            MetadataSchemas should be listed. Format:
            projects/{project}/locations/{location}/metadataStores/{metadatastore}
        page_size (int):
            The maximum number of MetadataSchemas to
            return. The service may return fewer.
            Must be in range 1-1000, inclusive. Defaults to
            100.
        page_token (str):
            A page token, received from a previous
            ``MetadataService.ListMetadataSchemas``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other provided parameters must match
            the call that provided the page token. (Otherwise the
            request will fail with INVALID_ARGUMENT error.)
        filter (str):
            A query to filter available MetadataSchemas
            for matching results.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)

    filter = proto.Field(proto.STRING, number=4)


class ListMetadataSchemasResponse(proto.Message):
    r"""Response message for
    ``MetadataService.ListMetadataSchemas``.

    Attributes:
        metadata_schemas (Sequence[google.cloud.aiplatform_v1beta1.types.MetadataSchema]):
            The MetadataSchemas found for the
            MetadataStore.
        next_page_token (str):
            A token, which can be sent as
            [MetadataService.ListMetadataSchemas.page_token][] to
            retrieve the next page. If this field is not populated,
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    metadata_schemas = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gca_metadata_schema.MetadataSchema,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))