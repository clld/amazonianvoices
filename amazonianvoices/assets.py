from pathlib import Path

from clld.web.assets import environment

import amazonianvoices


environment.append_path(
    Path(amazonianvoices.__file__).parent.joinpath('static').as_posix(),
    url='/amazonianvoices:static/')
environment.load_path = list(reversed(environment.load_path))
