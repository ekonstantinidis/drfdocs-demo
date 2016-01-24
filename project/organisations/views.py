from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from project.organisations.models import Organisation, Membership
from project.organisations.serializers import (
    CreateOrganisationSerializer, OrganisationMembersSerializer
)


class CreateOrganisationView(generics.CreateAPIView):
    """
    Allows users create an organisation.
    """

    serializer_class = CreateOrganisationSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        organisation = serializer.save()
        Membership.objects.create(
            organisation=organisation,
            user=self.request.user,
            is_owner=True
        )


class OrganisationMembersView(generics.ListAPIView):
    """
    List all the members for an organisation. User should be a member of that organisation.
    """

    serializer_class = OrganisationMembersSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        organisation = get_object_or_404(Organisation, slug=self.kwargs['slug'], members=self.request.user)
        return Membership.objects.filter(organisation=organisation)


class LeaveOrganisationView(generics.DestroyAPIView):
    """
    Users can leave an organisation if they are not the owner or the only admin.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self):
        organisation = get_object_or_404(Organisation, slug=self.kwargs['slug'])
        membership = get_object_or_404(Membership, organisation=organisation, user=self.request.user)
        return membership

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
