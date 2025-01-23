import os
from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from dagster_airbyte import AirbyteResource, load_assets_from_airbyte_instance
from pathlib import Path

resources = {
    "dbt": DbtCliResource(
        project_dir=os.getenv("DBT_PROJECT_DIR"),
        profiles_dir=os.getenv("DBT_PROFILES_DIR"),
    ),
    "airbyte_instance": AirbyteResource(
        host="localhost",
        port="8000",
        # If using basic auth, include username and password
        username="milheim05@gmail.com",
        password=os.getenv("AIRBYTE_PASSWORD")
    )
}

@dbt_assets(manifest=Path(os.getenv("DBT_MANIFEST_DIR"), "manifest.json"))
def my_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

airbyte_assets = load_assets_from_airbyte_instance(resources.get("airbyte_instance"), key_prefix=["raw_data"])