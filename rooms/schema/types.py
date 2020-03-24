from graphene import relay
from graphene_django import DjangoObjectType

from rooms.models import Room, Client, Reservation


class RoomNode(DjangoObjectType):
    class Meta:
        model = Room
        filter_fields = {
            'number': ['contains', 'startswith', ],
        }
        interfaces = (relay.Node, )


class ReservationNode(DjangoObjectType):
    class Meta:
        model = Reservation
        interfaces = (relay.Node, )


class ClientNode(DjangoObjectType):
    class Meta:
        model = Client
        interfaces = (relay.Node, )
