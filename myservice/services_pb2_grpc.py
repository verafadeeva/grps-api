# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services_pb2 as services__pb2


class MyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Service1 = channel.unary_unary(
                '/MyService/Service1',
                request_serializer=services__pb2.Service1Request.SerializeToString,
                response_deserializer=services__pb2.Empty.FromString,
                )
        self.Service2 = channel.unary_unary(
                '/MyService/Service2',
                request_serializer=services__pb2.Service2Request.SerializeToString,
                response_deserializer=services__pb2.Empty.FromString,
                )
        self.Service3 = channel.unary_unary(
                '/MyService/Service3',
                request_serializer=services__pb2.Service3Request.SerializeToString,
                response_deserializer=services__pb2.Empty.FromString,
                )
        self.Service4 = channel.unary_unary(
                '/MyService/Service4',
                request_serializer=services__pb2.Service4Request.SerializeToString,
                response_deserializer=services__pb2.Empty.FromString,
                )


class MyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Service1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Service2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Service3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Service4(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Service1': grpc.unary_unary_rpc_method_handler(
                    servicer.Service1,
                    request_deserializer=services__pb2.Service1Request.FromString,
                    response_serializer=services__pb2.Empty.SerializeToString,
            ),
            'Service2': grpc.unary_unary_rpc_method_handler(
                    servicer.Service2,
                    request_deserializer=services__pb2.Service2Request.FromString,
                    response_serializer=services__pb2.Empty.SerializeToString,
            ),
            'Service3': grpc.unary_unary_rpc_method_handler(
                    servicer.Service3,
                    request_deserializer=services__pb2.Service3Request.FromString,
                    response_serializer=services__pb2.Empty.SerializeToString,
            ),
            'Service4': grpc.unary_unary_rpc_method_handler(
                    servicer.Service4,
                    request_deserializer=services__pb2.Service4Request.FromString,
                    response_serializer=services__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Service1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyService/Service1',
            services__pb2.Service1Request.SerializeToString,
            services__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Service2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyService/Service2',
            services__pb2.Service2Request.SerializeToString,
            services__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Service3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyService/Service3',
            services__pb2.Service3Request.SerializeToString,
            services__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Service4(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyService/Service4',
            services__pb2.Service4Request.SerializeToString,
            services__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
