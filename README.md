# Discord Nitro Generator

**Note:** This exploit has been reported directly to Discord and a fix has been applied as of 21/12/2023. All information in this document is thusly outdated and exists for educational purposes only.

This Python script automates the generation of free one-month Discord Nitro trial URLs by exploiting a security oversight in Opera GX's current Discord Nitro promotion. 

## Installation

1. Clone the repo:
```bash
git clone https://github.com/FrostemanNeogard/DiscordNitroGenerator
```
2. Install the "requests" pip package:
```bash
cd DiscordNitroGenerator
pip install requests
```

## Usage

Run the python program. This will generate a `.txt` file in a seperate "outputs" directory which will contain the generated URLs.
To change the amount of URLs generated, simply modify the `DESIRED_ITERATIONS` variable in `main.py` to whatever number you please. It is set to 3 by default as to not send too many network requests at once.

## How does this work?

Opera GX is currently running a promotion where users of their browser can claim a free one month subscription of Discord Nitro.
The promotion is held at https://www.opera.com/gx/discord-nitro#how_to_claim.

The promotion process involves making a POST request to https://api.discord.gx.games/v1/direct-fulfillment, which returns a one-time-use JSON web token (JWT). Simultaneously, a new tab opens with a long URL for redeeming the trial.

Just for fun, here is the method which creates said URL:
```javascript
                this.generateAndShowPromoUrl = async t=>{
                    localStorage.setItem(this.SAVED_UUID, t);
                    const e = await this.initRequestToDiscord(t)
                      , r = `${this.DISCORD_BASE_URL}/${this.PROMOTION_ID}/${e.token}`;
                    e && window.open(r, "_blank")
                }
```

The Python script replicates this process by fetching the JWT and constructing a unique URL for trial redemption.
The security flaw lies in the fact that the Discord API call requires a partnerUserId in the body, and this can be very easily obtained from the network tab in the developer tools. This partnerUserId is **not** single-use, therefore we can use the exact one Opera GX uses.
By mimicking the API request with the same payload to https://api.discord.gx.games/v1/direct-fulfillment, a new, valid JWT can be acquired. Appending this JWT to the base Discord URL creates a functional Discord Nitro trial URL.

## Disclaimer

This script is provided for educational purposes only. The use of this script for any malicious or unauthorized activities is strictly prohibited.
The developers disclaim any responsibility for the consequences of using this script outside of ethical and legal boundaries.
