import discord


class Dropdown(discord.ui.Select):
    def __init__(
        self,
        user_id: int,
    ):

        print(
            "Initiating dropdown",
            user_id,
        )

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label=opt[0], emoji=opt[1])
            if isinstance(opt, tuple)
            else discord.SelectOption(label=opt)
            for opt in ["A", "B", "C", "D"]
        ]

        # prepare the dropdown
        super().__init__(
            placeholder="Select an option",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        # called once dropdown option selected
        user_id = interaction.user.id
        print("User", user_id)
        print("Selection: ", self.values[0])


class DropdownView(discord.ui.View):
    def __init__(self, user_id: int):
        super().__init__()

        # Adds the dropdown to our view object.
        # Pass on kwargs
        self.add_item(
            Dropdown(
                user_id=user_id,
            )
        )
