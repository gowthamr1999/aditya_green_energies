from django.core.management.base import BaseCommand
from main.models import About, Benefit, ContactInfo, Service, Testimonial


class Command(BaseCommand):
    help = "Seed initial website data (services, benefits, about, contact, testimonials)."

    def handle(self, *args, **options):
        self.seed_services()
        self.seed_benefits()
        self.seed_about()
        self.seed_contact_info()
        self.seed_testimonials()
        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully."))

    def seed_services(self):
        services = [
            {
                "title": "Solar Panel Installation",
                "icon": "sun",
                "description": "Complete rooftop and ground-mount solar installation for homes and businesses.",
                "features": [
                    "Site survey and system design",
                    "High-efficiency solar modules",
                    "Professional installation",
                    "Net metering support",
                ],
                "order": 1,
            },
            {
                "title": "Solar Maintenance",
                "icon": "wrench",
                "description": "Preventive and corrective maintenance to maximize output and system life.",
                "features": [
                    "Panel cleaning",
                    "Electrical health checks",
                    "Inverter diagnostics",
                    "Performance optimization",
                ],
                "order": 2,
            },
            {
                "title": "Energy Consultation",
                "icon": "badge-indian-rupee",
                "description": "Custom ROI and sizing guidance to reduce your electricity bills.",
                "features": [
                    "Consumption analysis",
                    "System sizing",
                    "Savings projection",
                    "Government subsidy guidance",
                ],
                "order": 3,
            },
        ]

        for service in services:
            obj, created = Service.objects.update_or_create(
                title=service["title"],
                defaults=service,
            )
            self.log_action("Service", obj.title, created)

    def seed_benefits(self):
        benefits = [
            {
                "title": "Lower Electricity Bills",
                "icon": "wallet",
                "description": "Reduce monthly power costs significantly with solar energy generation.",
                "order": 1,
            },
            {
                "title": "Clean Renewable Energy",
                "icon": "leaf",
                "description": "Cut carbon emissions and support a sustainable future.",
                "order": 2,
            },
            {
                "title": "Higher Property Value",
                "icon": "building-2",
                "description": "Solar-equipped properties are more attractive to buyers and tenants.",
                "order": 3,
            },
            {
                "title": "Reliable Long-Term Returns",
                "icon": "trending-up",
                "description": "Enjoy stable returns from decades of solar power generation.",
                "order": 4,
            },
        ]

        for benefit in benefits:
            obj, created = Benefit.objects.update_or_create(
                title=benefit["title"],
                defaults=benefit,
            )
            self.log_action("Benefit", obj.title, created)

    def seed_about(self):
        defaults = {
            "title": "About Aditya Green Energies",
            "description": (
                "We are a trusted partner of Waaree Energies, delivering premium solar "
                "solutions in Bengaluru and beyond. Our mission is to empower homes and "
                "businesses with sustainable energy that saves money and protects the planet."
            ),
            "image": "",
        }

        about = About.objects.first()
        if about:
            for field, value in defaults.items():
                setattr(about, field, value)
            about.save()
            self.stdout.write("Updated About section")
        else:
            About.objects.create(**defaults)
            self.stdout.write("Created About section")

    def seed_contact_info(self):
        defaults = {
            "phone": "+91 9535156339",
            "email": "adityagreenenergies@gmail.com",
            "address": "Sy No 184/4, Sarjapura Main Road, Dommasandra, Bengaluru, Karnataka, 562125",
            "whatsapp": "+919535156339",
            "facebook": "",
            "instagram": "",
        }

        contact = ContactInfo.objects.first()
        if contact:
            for field, value in defaults.items():
                setattr(contact, field, value)
            contact.save()
            self.stdout.write("Updated ContactInfo")
        else:
            ContactInfo.objects.create(**defaults)
            self.stdout.write("Created ContactInfo")

    def seed_testimonials(self):
        testimonials = [
            {
                "name": "Ramesh Kumar",
                "location": "Bengaluru",
                "rating": 5,
                "testimonial": "Installation was smooth and my power bill dropped drastically. Highly recommended.",
                "is_featured": True,
            },
            {
                "name": "Shwetha N",
                "location": "Sarjapura",
                "rating": 5,
                "testimonial": "Professional team and excellent support throughout subsidy and net-metering process.",
                "is_featured": True,
            },
            {
                "name": "Imran Pasha",
                "location": "Whitefield",
                "rating": 4,
                "testimonial": "Very good service quality and clear communication from survey to commissioning.",
                "is_featured": False,
            },
        ]

        for item in testimonials:
            obj, created = Testimonial.objects.update_or_create(
                name=item["name"],
                location=item["location"],
                defaults=item,
            )
            self.log_action("Testimonial", obj.name, created)

    def log_action(self, model_name, identifier, created):
        action = "Created" if created else "Updated"
        self.stdout.write(f"{action} {model_name}: {identifier}")
