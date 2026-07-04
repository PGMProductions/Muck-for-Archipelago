from worlds.LauncherComponents import Component, Type, components, launch, icon_paths


def run_client(*args: str) -> None:
    from .client.launch import LaunchClient

    launch(LaunchClient, name="APQuest Client", args=args)

components.append(
    Component(
        "muck client",
        func=run_client,
        game_name="Muck",
        component_type=Type.CLIENT,
        supports_uri=True,
        icon='MUCK Icon'
    )
)
icon_paths['MUCK Icon'] = f"ap:{__name__}/muck.png"