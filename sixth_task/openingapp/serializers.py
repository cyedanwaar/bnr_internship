from rest_framework import serializers
from .models import Recruiter, Proposal, Opening, OpeningDetail, Partner
from drf_writable_nested import WritableNestedModelSerializer


class PartnerSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Partner
        exclude = ['opening_details', 'id']


class OpeningDetailSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    partners = PartnerSerializer(required=False, many=True)

    class Meta:
        model = OpeningDetail
        fields = '__all__'
    
    def create(self, validated_data):
        partner_data = validated_data.pop('partners', [])

        od_instance = OpeningDetail.objects.create(**validated_data)

        for objs in partner_data:
            Partner.objects.create(opening_details=od_instance, **objs)

        return od_instance
    

class RecruiterSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    recruiter_opening = OpeningDetailSerializer(required=False, many=True)
    class Meta:
        model = Recruiter
        fields = '__all__'
    
    def create(self, validated_data):

        od_data = validated_data.pop('recruiter_opening', [])

        recruiter_instance = Recruiter.objects.create(**validated_data)

        for objs in od_data:
            OpeningDetail.objects.create(recruiter=recruiter_instance, **objs)

        return recruiter_instance


class ProposalSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    proposal_opening = OpeningDetailSerializer(required=False, many=True)
    class Meta:
        model = Proposal
        fields = '__all__'
    
    def create(self, validated_data):

        od_data = validated_data.pop('proposal_opening', [])

        proposal_instance = Proposal.objects.create(**validated_data)

        for objs in od_data:
            OpeningDetail.objects.create(proposal=proposal_instance, **objs)
        
        return proposal_instance


class OpeningSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    details = OpeningDetailSerializer(required=False, many=True)

    class Meta:
        model = Opening
        fields = '__all__'
    
    def create(self, validated_data):

        od_data = validated_data.pop('details', [])

        opening_instance = Opening.objects.create(**validated_data)


        for od_obj in od_data:
            partners_data = od_obj.pop('partners', [])  # Access 'partners' key for each detail
            od_instance = OpeningDetail.objects.create(openings=opening_instance, **od_obj)

            for partner_obj in partners_data:
                Partner.objects.create(opening_details=od_instance, **partner_obj)

        return opening_instance

