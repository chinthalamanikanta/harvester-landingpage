from nicegui import ui
from translations import translations
from components.navbar import create_navbar
from components.hero import create_hero
from components.about import create_about
from components.features import create_features
from components.farmer_flow import create_farmer_flow
from components.owner_flow import create_owner_flow
from components.stats import create_stats
from components.screenshots import create_screenshots
from nicegui import ui, app
from components.contact import contact_section
from components.testimonials import (
    testimonials_section,
    stats_section,
    trust_section,
)

app.add_static_files('/static', 'static')

ui.colors(
    primary="#2E7D32",
    secondary="#4CAF50",
    accent="#FFC107",
)

create_navbar()
create_hero()
create_about()
create_features()
create_farmer_flow()
create_owner_flow()
create_stats()
create_screenshots()
testimonials_section()

stats_section()

trust_section()
contact_section()

language = "en"


ui.run(
    host="0.0.0.0",
    port=8080,
    title="Harvester Connect",
    reload=True,
)
