"""Client and server classes for gRPC services."""
import grpc


class AugmentInitStub(object):
    """The Stub for connecting to the Augment init service."""

    def __init__(self, channel, avroserialhelper):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.initAugment = channel.unary_stream(
            "/templateaapi.AugmentInit/initTemplate",
            request_serializer=avroserialhelper.avro_serializer,
            response_deserializer=avroserialhelper.avro_deserializer,
        )


class AugmentInitServicer(object):
    """The servicer definition for initiating jobs with the Augment pipeline."""

    def initAugment(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AugmentInitServicer_to_server(servicer, server, avroserialhelper):
    """The actual methods for sending and receiving RPC calls."""
    rpc_method_handlers = {
        "initAugment": grpc.unary_stream_rpc_method_handler(
            servicer.initAugment,
            request_deserializer=avroserialhelper.avro_deserializer,
            response_serializer=avroserialhelper.avro_serializer,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "templateaapi.AugmentInit", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


class AugmentInit(object):
    """The definition of the Augment gRPC API and stream connections."""

    @staticmethod
    def initAugment(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/templateaapi.AugmentInit/initTemplate",
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class AugmentMonitorStub(object):
    """The Stub for connecting to the Augment Monitor service."""

    def __init__(self, channel, avroserialhelper):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.monitorAugment = channel.unary_stream(
            "/templateaapi.AugmentMonitor/monitorTemplate",
            request_serializer=avroserialhelper.avro_serializer,
            response_deserializer=avroserialhelper.avro_deserializer,
        )


class AugmentMonitorServicer(object):
    """The servicer definition for monitoring jobs already submitted to the Augment pipeline."""

    def monitorAugment(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AugmentMonitorServicer_to_server(servicer, server, avroserialhelper):
    """The actual methods for sending and receiving RPC calls."""
    rpc_method_handlers = {
        "monitorAugment": grpc.unary_stream_rpc_method_handler(
            servicer.monitorAugment,
            request_deserializer=avroserialhelper.avro_deserializer,
            response_serializer=avroserialhelper.avro_serializer,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "templateaapi.AugmentMonitor", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


class AugmentMonitor(object):
    """The definition of the Monitor gRPC API and stream connections."""

    @staticmethod
    def monitorAugment(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/templateaapi.AugmentMonitor/monitorTemplate",
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
