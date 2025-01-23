from dagster import Definitions, load_assets_from_modules, ScheduleDefinition, define_asset_job, AssetSelection

from .assets import resources

big_star_job = define_asset_job("big_star_job", selection=AssetSelection.all())

big_star_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule="0 * * * *", # @hourly
)

defs = Definitions(
    assets=load_assets_from_modules([assets]), 
    resources=resources,
    jobs=[big_star_job],
    schedules=[big_star_schedule]
)