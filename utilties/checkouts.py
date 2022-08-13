import discord


def check_admin_rights(interaction: discord.Interaction) -> None:
    if interaction.guild.get_role(898307915348332614) not in interaction.user.roles:
        raise discord.app_commands.AppCommandError('User access denied')
