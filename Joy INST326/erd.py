from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.erd.crowsfoot import OneToMany, ManyToMany, OneToOne

with Diagram("Exotic Events ERD", show=False, direction="TB"):

    with Cluster("Event"):
        event = Custom("Event", "/mnt/data/eshop_architecture.png")
        event_id = Custom("Event ID", "/mnt/data/eshop_architecture.png")
        event_name = Custom("Event Name", "/mnt/data/eshop_architecture.png")
        event_type = Custom("Event Type", "/mnt/data/eshop_architecture.png")
        date_time = Custom("Date and Time", "/mnt/data/eshop_architecture.png")
        venue_id = Custom("Venue ID", "/mnt/data/eshop_architecture.png")
        organizer_id = Custom("Organizer ID", "/mnt/data/eshop_architecture.png")
        description = Custom("Description", "/mnt/data/eshop_architecture.png")
        expected_attendees = Custom("Expected Attendees", "/mnt/data/eshop_architecture.png")

    with Cluster("Attendee"):
        attendee = Custom("Attendee", "/mnt/data/eshop_architecture.png")
        attendee_id = Custom("Attendee ID", "/mnt/data/eshop_architecture.png")
        first_name = Custom("First Name", "/mnt/data/eshop_architecture.png")
        last_name = Custom("Last Name", "/mnt/data/eshop_architecture.png")
        email = Custom("Email", "/mnt/data/eshop_architecture.png")
        phone_number = Custom("Phone Number", "/mnt/data/eshop_architecture.png")
        ticket_type = Custom("Ticket Type", "/mnt/data/eshop_architecture.png")
        registration_date_time = Custom("Registration Date and Time", "/mnt/data/eshop_architecture.png")

    with Cluster("Venue"):
        venue = Custom("Venue", "/mnt/data/eshop_architecture.png")
        venue_name = Custom("Venue Name", "/mnt/data/eshop_architecture.png")
        address = Custom("Address", "/mnt/data/eshop_architecture.png")
        capacity = Custom("Capacity", "/mnt/data/eshop_architecture.png")
        contact_person = Custom("Contact Person", "/mnt/data/eshop_architecture.png")
        contact_email = Custom("Contact Email", "/mnt/data/eshop_architecture.png")
        contact_phone_number = Custom("Contact Phone Number", "/mnt/data/eshop_architecture.png")

    with Cluster("Organizer"):
        organizer = Custom("Organizer", "/mnt/data/eshop_architecture.png")
        organizer_id = Custom("Organizer ID", "/mnt/data/eshop_architecture.png")
        organizer_first_name = Custom("First Name", "/mnt/data/eshop_architecture.png")
        organizer_last_name = Custom("Last Name", "/mnt/data/eshop_architecture.png")
        organizer_email = Custom("Email", "/mnt/data/eshop_architecture.png")
        organizer_phone_number = Custom("Phone Number", "/mnt/data/eshop_architecture.png")
        organization_name = Custom("Organization Name", "/mnt/data/eshop_architecture.png")
        role_or_title = Custom("Role or Title", "/mnt/data/eshop_architecture.png")
        organizer_address = Custom("Address", "/mnt/data/eshop_architecture.png")
        experience_level = Custom("Experience Level", "/mnt/data/eshop_architecture.png")
        specialization = Custom("Specialization", "/mnt/data/eshop_architecture.png")

    event >> OneToMany(venue)
    event >> ManyToMany(attendee, label="Event_Attendee")
    event >> OneToMany(organizer)
