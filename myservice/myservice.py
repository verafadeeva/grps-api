from google.protobuf.json_format import MessageToDict
from concurrent import futures
import asyncio

import grpc
from pydantic import ValidationError

import services_pb2_grpc
import services_pb2
from models import Servise1Model, Servise2Model, Servise3Model, Servise4Model
from dbshema import create_a_engine, DataHandler


class MyService(services_pb2_grpc.MyServiceServicer):
    def __init__(self) -> None:
        super().__init__()
        self.connection = create_a_engine()

    async def Service1(self, request, context):
        try:
            data = Servise1Model(**MessageToDict(
                request, preserving_proto_field_name=True
            ))
        except ValidationError as err:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, err.json(indent=None))
        transaction = await self.connection.asend(None)
        async with transaction.begin():
            if data.id is not None:
                DataHandler(data).update()
            else:
                DataHandler(data).create()
        return services_pb2.Empty()

    async def Service2(self, request, context):
        try:
            data = Servise2Model(**MessageToDict(
                request, preserving_proto_field_name=True
            ))
        except ValidationError as err:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, err.json(indent=None))
        transaction = await self.connection.asend(None)
        async with transaction.begin():
            if data.id is not None:
                DataHandler(data).update()
            else:
                DataHandler(data).create()
        return services_pb2.Empty()

    async def Service3(self, request, context):
        try:
            data = Servise3Model(**MessageToDict(
                request, preserving_proto_field_name=True
            ))
        except ValidationError as err:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, err.json(indent=None))
        transaction = await self.connection.asend(None)
        async with transaction.begin():
            DataHandler(data).create()
        return services_pb2.Empty()

    async def Service4(self, request, context):
        try:
            data = Servise4Model(**MessageToDict(
                request, preserving_proto_field_name=True
            ))
        except ValidationError as err:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, err.json(indent=None))
        transaction = await self.connection.asend(None)
        async with transaction.begin():
            DataHandler(data).create()
        return services_pb2.Empty()


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_MyServiceServicer_to_server(
        MyService(), server
    )
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(serve())
