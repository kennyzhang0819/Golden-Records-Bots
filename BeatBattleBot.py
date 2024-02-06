import discord
from discord.ext import commands
from submission import Submission

TOKEN = ''
intents = discord.Intents(messages=True, reactions=True, guilds=True, members=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=intents)

battle_name = None
battle_state = None
submissions = {}
winner = None

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occurred: {str(error)}")

@bot.command()
async def doc(ctx):
    general_commands = (
        "**General Commands (accessible by all):**\n"
        "`!submit LINK (optional)@collaborator`: To submit your beat.\n"
        "`!status`: To get the status of the ongoing battle.\n"
    )

    exec_commands = (
        "**Exec Commands:**\n"
        "`!start_battle NAME`: To start a beat battle with the specified name.\n"
        "`!cancel_battle`: To cancel the ongoing beat battle.\n"
        "`!getSubmissions`: To get a list of all submissions.\n"
        "`!start_voting`: To transition from submission to voting phase.\n"
        "`!end_battle`: To end the battle and announce the winner.\n"
    )

    await ctx.send(f"{general_commands}\n{exec_commands}")



@bot.command()
@commands.has_role('Exec')
async def start_battle(ctx, name: str = None):
    global battle_state, battle_name
    if not name:
        await ctx.send("Please provide a name for the battle! Follow the format: `!start_battle NAME`.")
        return

    if battle_state:
        await ctx.send(f"Beat Battle - {battle_name} is already ongoing!")
        return

    battle_name = name
    battle_state = 'submission'
    await ctx.send(f"Started Beat Battle - {battle_name}! Waiting for submissions.")

@bot.command()
async def submit(ctx, link: str = None, *collab: discord.Member):
    if not link:
        await ctx.send("Please provide a link to your beat! Follow the format: `!submit YOUR_LINK`. You can also add collaborators by following the format: `!submit YOUR_LINK @COLLABORATOR1 @COLLABORATOR2 ...`.")
        return
    if battle_state == 'submission':
        collaborators_mentions = [collaborator.mention for collaborator in collab]
        submission = Submission(ctx.author, link, collab)
        submissions[submission.author] = submission
        if collaborators_mentions:
            await ctx.send(f"{ctx.author.mention} has submitted a beat! Collaborators: {', '.join(collaborators_mentions)}")
        else:
            await ctx.send(f"{ctx.author.mention} has submitted a beat!")
    else:
        await ctx.send("No active battle or submission time has ended. Please wait for the next battle to start!")

@bot.command()
async def status(ctx):
    if not battle_state:
        await ctx.send("No active battle.")
        return

    status_msg = (
        f"**Beat Battle Status for '{battle_name}':**\n"
        f"Current Stage: {battle_state}\n"
        f"Participants: {', '.join(map(str, submissions.keys()))}\n"
        f"Winner: {winner.mention if winner else 'None'}"
    )
    await ctx.send(status_msg)

@bot.command()
@commands.has_role('Exec')
async def cancel_battle(ctx):
    await clean_up()
    await ctx.send(f"Beat Battle - {battle_name} has been cancelled.")

@bot.command()
@commands.has_role('Exec')
async def getSubmissions(ctx):
    await ctx.send(f"Submissions for Beat Battle - {battle_name}: {submissions}")

@bot.command()
@commands.has_role('Exec')
async def start_voting(ctx):
    global battle_state
    if battle_state == 'submission':
        battle_state = 'voting'
        await post_submissions_for_voting()
    else:
        await ctx.send("Beat Battle is either not active or not in the submission phase.")

@bot.command()
@commands.has_role('Exec')
async def end_battle(ctx):
    global battle_state
    if battle_state == 'voting':
        battle_state = None
        await announce_winner()
    else:
        await ctx.send("Beat Battle is either not active or not in the voting phase.")

async def post_submissions_for_voting():
    channel = bot.get_channel(123)
    await channel.send(f"Voting has started for Beat Battle - {battle_name}! Vote for your favorite beat by reacting to the message.")
    for submission in submissions.values():
        if submission.collaborators:
            msg = await channel.send(f"{submission.author.mention}, {', '.join([collab.mention for collab in submission.collaborators])}: {submission.link}")
        else:
            msg = await channel.send(f"{submission.author.mention}: {submission.link}")
        await msg.add_reaction("🧡")
        submission.add_msg(msg)


async def announce_winner():
    channel = bot.get_channel(123)
    await channel.send(f"Voting has ended for Beat Battle '{battle_name}'! Calculating the winner...")

    msg_reactions = {}

    print(f"DEBUG: Submissions count: {len(submissions)}")  # Debugging line

    for submission in submissions.values():
        # Debugging lines
        print(
            f"DEBUG: Submission from {submission.author.name}. Message ID: {submission.msg.id if submission.msg else 'None'}")

        if submission.msg and submission.msg.reactions:
            for reaction in submission.msg.reactions:
                print(f"DEBUG: Reaction: {reaction.emoji}, Count: {reaction.count}")  # Debugging line

        msg_reactions[submission] = submission.msg.reactions[0].count if submission.msg and submission.msg.reactions else 0

    winner_submission = max(msg_reactions, key=msg_reactions.get)

    print(
        f"DEBUG: Winner is {winner_submission.author.name} with {msg_reactions[winner_submission]} votes.")  # Debugging line

    await channel.send(
        f"Beat Battle '{battle_name}' ended. HUGE CONGRATS TO THE WINNER: {winner_submission.author.mention}!")
    await clean_up()


async def clean_up():
    global battle_state, submissions, winner, battle_name
    battle_name = None
    battle_state = None
    submissions.clear()
    winner = None

bot.run(TOKEN)
