


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines={}
    for event in events:
        if event.machine not in machines:
            machines[event.machine]=set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)    
    return machines        


def generate_report(machines):
    for machine,users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine,user_list))



class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:56','login','system1','Pushkar'),
    Event('2020-01-21 11:45:56','login','system1','Anda Singh'),
    Event('2020-01-21 10:45:56','logout','system2','Prince'),
    # Event('2020-01-21 10:45:56','login','system2','Prince'),
    Event('2020-01-21 12:41:56','login','system3','Lala Kapur'),
    # Event('2020-01-21 10:45:56','logout','system2','Prince'),
    Event('2020-01-21 11:42:56','login','system1','Mohit'),
 ]       


users = current_users(events)
print(users)
generate_report(users)