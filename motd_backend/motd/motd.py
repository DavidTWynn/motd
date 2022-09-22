#!/usr/env/bin python3.10
import jinja2


def main() -> None:
    template_input = {
        "street_address": "9516 Snow Heights Cir NE",
        "city": "Albuquerque",
        "state": "NM",
        "zip": "87112",
        "model": "Cisco IOSvL2",
        "uptime": "2 weeks, 2 days, 5 hours, 23 minutes",
        "last_change": "23:43:51 UTC Wed Sep 21 2022",
        "cpu": "five seconds: 25%/0%; one minute: 15%",
        "memory": "15%",
        "uplink_util": "5%",
    }

    banner = create_basic_banner(**template_input)

    print(banner)


def create_basic_banner(
    street_address: str,
    city: str,
    state: str,
    zip: str,
    model: str,
    uptime: str,
    last_change: str,
    cpu: str,
    memory: str,
    uplink_util: str,
) -> str:
    """Creates basic banner motd based on passed arguments."""

    template = import_template("motd_template.j2")

    # Send dictionary of key value pairs for variables in template
    # Using locals to send exactly whats sent to this function
    template_output = template.render(locals())

    return template_output


def import_template(template_name: str) -> jinja2.Template:
    """Takes file name and imports template based on pre-defined location."""
    # Prepare to import template
    template_file_location = "motd_backend/motd/templates/"
    template_loader = jinja2.FileSystemLoader(template_file_location)
    environment = jinja2.Environment(loader=template_loader)

    # Import template for rendering
    template = environment.get_template(template_name)

    return template


if __name__ == "__main__":
    main()
