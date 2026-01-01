from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exists"
)

IncorectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorect Email or Password"
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired"
)

TokenNoExistException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token does not exist"
)

IncorectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorect token format"
)

InvalidUserException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid user"
)

RoomCannotBeBooked =  HTTPException(
    status_code =status.HTTP_409_CONFLICT,
    detail="All rooms are booked"
)

DateFromCannotBeAfterDateTo = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Дата заезда не может быть позже даты выезда"
)

CannotBookHotelForLongPeriod = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Невозможно забронировать отель сроком более месяца"
)