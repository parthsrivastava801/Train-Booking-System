from rest_framework import serializers
from .models import Train, Booking

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'booking_timestamp']

    def validate(self, data):
        train = data['train']
        seat_number = data['seat_number']

        if seat_number > train.total_seats:
            raise serializers.ValidationError("Seat number exceeds total seats on the train.")

        # Check if seat is already booked for this train
        if Booking.objects.filter(train=train, seat_number=seat_number).exists():
            raise serializers.ValidationError(f"Seat number {seat_number} is already booked for this train.")

        if train.seats_available <= 0:
            raise serializers.ValidationError("No seats available on this train.")

        return data

    def create(self, validated_data):
        train = validated_data['train']

        # Decrement the available seats
        train.seats_available -= 1
        train.save()

        return super().create(validated_data)
