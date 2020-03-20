from datetime import datetime, timedelta


def validate_conditions(conditions):
    counter = 0

    for condition in conditions:
        if not condition.get('hours'):
            counter += 1
        if condition.get('hours', 0) > 24:
            raise ValueError('Hours cannot be > 24.')
        if condition.get('percent') > 100:
            raise ValueError('Percent cannot be > 100%')
        if condition.get('percent') < 0:
            raise ValueError('Percent cannot be < 0%')

    if counter != 1:
        raise ValueError('Invalid conditions.')


def ensure_conditions(conditions):
    for condition in conditions:
        if not condition.get('hours'):
            condition['hours'] = 0
    return conditions

def sort_conditions(conditions):
    return sorted(conditions, key = lambda c: c['hours'], reverse = True)

def get_current_condition(conditions, start, now):
    searched_hours = start - now
    pos = 0

    if searched_hours.days >= 1:
        return conditions[0]['percent']

    for i in conditions:
        if i.get('hours') < searched_hours.seconds/3600:
            return conditions[pos]['percent']
        pos += 1

    return conditions[pos-1]['percent']


def get_cancellation_fee(price, percent):
    return price * (percent / 100)


def get_cancellation_policy(conditions, price, start, now):

    assert now < start

    assert price > 0

    validate_conditions(conditions)

    ensured_conditions = ensure_conditions(conditions)

    sorted_conditions = sort_conditions(ensured_conditions)

    percent = get_current_condition(sorted_conditions, start, now)

    return get_cancellation_fee(price, percent)

def main():
    now = datetime.now()
    booking_start = now + timedelta(hours=0)
    price = 1000
    conditions = [
        {'hours': 24, 'percent': 10},
        {'hours': 12, 'percent': 50},
        {'hours': 6, 'percent': 80},
        {'percent': 100}
    ]

    result = get_cancellation_policy(
        conditions,
        price,
        booking_start,
        now
    )
    print(result)


if __name__ == '__main__':
    main()

