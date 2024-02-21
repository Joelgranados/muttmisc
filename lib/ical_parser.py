import json
import email
import icalendar

def when_str_of_start_end(s, e):
    date_format = "%a, %d %b %Y at %H:%M"
    until_format = "%H:%M" if s.date() == e.date() else date_format
    return "%s -- %s" % (s.strftime(date_format), e.strftime(until_format))

class IcalParser:
    ical_events=[]

    def __init__(self, msg_str):
        e_msgs = email.message_from_string(msg_str)
        for e_msg in e_msgs.walk():
            try:
                self.add_to_ical_events(e_msg.get_payload())
            except:
                continue

        if len(self.ical_events) > 0:
            return

        # try with just the string
        try:
            self.add_to_ical_events(msg_str)
        except:
            pass

        if len(self.ical_events) < 1:
            raise Exception("Could not find a calendar event in the mail")

    def add_to_ical_events(self, m):
        ical_obj = icalendar.Calendar.from_ical(m)
        for component in ical_obj.walk():
            if component.name == "VEVENT":
                self.ical_events.append(component)

    def to_json(self):
        if len(self.ical_events) < 1:
            raise Exception("Could not find a calendar event in the mail")

        ical_vevent = self.ical_events[0]
        title = str(ical_vevent.get('summary'))
        start = ical_vevent.get('dtstart').dt
        description = str(ical_vevent.get('description'))

        return json.dumps({
            "content" : title,
            "due_string" : str(start),
            "description" : description
        })

    def __str__(self):
        if len(self.ical_events) < 1:
            raise Exception("Could not find a calendar event in the mail")

        ical_vevent = self.ical_events[0]
        title = str(ical_vevent.get('summary'))
        org = str(ical_vevent.get('organizer'))
        start = ical_vevent.get('dtstart').dt
        end = ical_vevent.get('dtend').dt
        location = str(ical_vevent.get('location'))
        description = str(ical_vevent.get('description'))
        attendee = ical_vevent.get('attendee')
        if description == 'None':
            description = "No Description available"
        if attendee is None:
            invitees = ["No Atendees available"]
        else:
            if isinstance(attendee, str):
                invitees = [ical_vevent['attendee']]
            else:
                invitees = [str(x) for x in attendee]

        ret_str = "="*70
        ret_str += "\n"
        ret_str +="MEETING INVITATION".center(70)
        ret_str += "\n"
        ret_str +="="*70
        ret_str += "\n"
        ret_str +="Event:\n\t%s" % title.encode('utf-8')
        ret_str += "\n"
        ret_str +="Organiser:\n\t%s" % org.encode('utf-8')
        ret_str += "\n"
        ret_str +="When:\n\t%s" % when_str_of_start_end(start, end).encode('utf-8')
        ret_str += "\n"
        ret_str +="Location:\n\t%s" % location.encode('utf-8')
        ret_str += "\n"
        ret_str +="---\n%s\n---" % description
        #ret_str +="---\n%s\n---" % description.encode('utf-8')
        ret_str += "\n"
        ret_str +="Invitees:"
        ret_str += "\n"
        for i in invitees:
            ret_str +="\t%s" % i.encode('utf-8')
            ret_str += "\n"

        return ret_str

