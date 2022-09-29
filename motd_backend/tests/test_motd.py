import pytest

import jinja2

from motd import motd


def test_import_jinja_template_is_template_object():
    template_file_location = "motd_template.j2"
    imported_template = motd.import_template(template_file_location)
    assert isinstance(imported_template, jinja2.Template)


@pytest.fixture
def setup_template() -> jinja2.Template:
    template_file_location = "motd_template.j2"
    imported_template = motd.import_template(template_file_location)
    return imported_template


def test_render_template(setup_template: jinja2.Template):
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
    template_output = setup_template.render(**template_input)

    expected_output = """\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                  Welcome to                  %
%           9516 Snow Heights Cir NE           %
%                 Albuquerque                  %
%                   NM 87112                   %
%                                              %
%             Model: Cisco IOSvL2              %
% Uptime: 2 weeks, 2 days, 5 hours, 23 minutes %
%  Last change: 23:43:51 UTC Wed Sep 21 2022   %
%  CPU five seconds: 25%/0%; one minute: 15%   %
%                 Memory: 15%                  %
%            Uplink utilization: 5%            %
%                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

    assert template_output == expected_output
