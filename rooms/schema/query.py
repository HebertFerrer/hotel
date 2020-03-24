import graphene
from graphene_django.filter import DjangoFilterConnectionField

from rooms.schema.types import RoomNode, ReservationNode, ClientNode


class Query(object):
    room = graphene.Node.Field(RoomNode)
    rooms = DjangoFilterConnectionField(RoomNode)
