# A Collaborative and Open Source News bot

## Dependencies
- bs4 (Beautiful Soup).
- pprint (Pretty Print).
- requests (The name already says it).
- discord (Discord integration).
- dotenv (.env file handler)

## Let me tell you what this bot does:
- Provides news for developers.
- Provides news for any source you want (to be a feature in future).
- Provide the link for the youtube video of the news searched (if exists).
- And many more features to be implemented in future.


## Whats / Hows?
- Bot Admin should have a role `Newspaper Admin`
- Bot has reloadable cogs
- current cogs - `{"news","general"}`

## Commands
- ~ `$load <cog>` - loads the `cog` again to the bot client 
- ~ `$unload <cog>` - unloads the `cog` again to the bot client 
- ~ `$reload <cog>` - unloads and loads the `cog` again to the bot client
- ~ `$logout` - logs out the bot client 
- `ping` - gives the latency of the bot client

>(Commands mentioned with `~` require Admin Role)