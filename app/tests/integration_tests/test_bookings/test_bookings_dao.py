

import datetime

from app.bookings.dao import BookingDAO


async def test_add_and_get_booking():
    new_booking = await BookingDAO.add(
        user_id=2,
        room_id=2,
        date_from=datetime.datetime.strptime("2025-06-10", "%Y-%m-%d").date(),
        date_to=datetime.datetime.strptime("2025-06-23", "%Y-%m-%d").date(),
    )
    assert new_booking.user_id == 2
    assert new_booking.room_id == 2

    new_booking = await BookingDAO.find_by_id(new_booking.id)

    assert new_booking is not None