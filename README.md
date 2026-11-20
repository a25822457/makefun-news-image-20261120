# Friday 20 November 2026: 40 stories, 7 regions, 15 illustrated, UTC timeline, date-checked

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/a25822457/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/a25822457/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

[make.fun competition — news-image-20261120](https://make.fun/c/news-image-20261120)

One front page of **Friday 20 November 2026**: 40 verified stories from 7 regions, 15 illustrated, a UTC timeline, and a markets strip. Every story below was checked against reporting dated 20 November 2026. Nothing here is from before 13 November.

**Caveat:** this image was built from stories reported up to about 06:00 UTC on 20 November, because the entry is built the same day. Later developments on 20 November are not in it. Every story it does contain was reported on Friday 20 November 2026.

## The 40 stories

| # | Story | What happened | Verified against |
| --- | --- | --- | --- |
| 1 | **Lead — Asia stocks crash on AI fears** | Nikkei −4.5%, Kospi −4.7%, MSCI Asia −2.5% — worst week since 2020. Anthropic's debut fails to calm the AI trade. | CNA · Nikkei Asia · TradingView |
| 2 | **Trump to announce trade deals today** | White House press conference after the Asia trip. | Newsbytes |
| 3 | **Fresh strike hits Kerch rail track** | Neptune missiles hit the Kerch rail viaduct; third strike this week. | Reuters via One Turn |
| 4 | Iran plans Kharg tanker convoy | Iran plans a convoy to defy the US blockade. | Newsbytes |
| 5 | 65,000 tents await entry to Gaza | Winterisation tents stuck at the border. | Scoop |
| 6 | European Commission hit by cyberattack | Major attack; employees' personal data at risk. | Times Now |
| 7 | UK pledges 1,000 drones for Ukraine | £260m package, announced in Berlin. | AppiSToS |
| 8 | US approves 900k AI chips for China | Nvidia/AMD chips approved in six months, US panel reveals. | Times Now |
| 9 | Yunus property catches fire | Property of Bangladesh's former leader Muhammad Yunus. | annagranules |
| 10 | US consortium wins Kenya minerals deal | Mrima Hill deal, defeating Chinese rivals. | annagranules |
| 11 | Trump pardons Pete Rose | Posthumous pardon for the late baseball star. | AppiSToS |
| 12 | USDA hit by cyber incident | Farmer aid systems disrupted. | Times Now |
| 13 | Antibiotics stop working, UN warns | Patients running out of options as antibiotics fail. | UN News via Scoop |
| 14 | Harvard: phone bans add learning | Cellphone bans yield one or two weeks' extra learning. | Newsbytes |
| 15 | Kirsten Davies named acting cyber chief | Named acting national cyber director after Cairncross was fired. | Times Now |
| 16 | Trump holds off Iran strikes till New Year | Despite pressure from Israel. | Times Now |
| 17 | Trump weighs new Iran strikes | New round under consideration. | Times Now |
| 18 | Senate Democrats move to block Iran funds | Van Hollen leads the bid. | One Turn |
| 19 | Iran demands emergency OIC meeting on Gaza | Foreign ministers' meeting. | annagranules |
| 20 | Bus crash in Abdanan kills 13 | Protests follow; 7 arrested. | Newsbytes |
| 21 | Putin invites European leaders to Moscow | As Europe pushes for a role in Ukraine talks. | Times Now |
| 22 | Putin: war with Europe 'nonsense' | Dismisses the talk. | Newsbytes |
| 23 | RAF airbase siren, shelter in place | Home to ~7,000 US troops. | Times Now |
| 24 | Europe youth action called for today | Cost of living, housing, education. | AppiSToS |
| 25 | COP31 wraps up, fossil fuels cut | Near-final texts drop the fossil-fuel transition. | Scoop |
| 26 | NATO Edge 2026 wraps in Turkey | NATO exercise ends. | annagranules |
| 27 | Crimea food sales restricted | After the Kerch Bridge attack. | annagranules |
| 28 | Trump: North Korea meeting possible | After Shenzhen talks. | Newsbytes |
| 29 | Manila arrests: 6 children still held | Mass arrests in Manila. | Scoop |
| 30 | Trump dozes off during Xi address | Caught on camera at the APEC summit. | Times Now |
| 31 | Xi: Asia-Pacific must not turn back | To APEC leaders. | Scoop |
| 32 | Cyclone Xavier track updated | RSMC Nadi revises the forecast. | RSMC Nadi |
| 33 | Trump responds after Musk 'Not MAGA' | Musk says he is 'Not MAGA'. | Times Now |
| 34 | Trump admin seeks dismissal of Alaska case | Senate certification challenge. | Newsbytes |
| 35 | US Army pauses Iowa blast | 5-ton lead azide detonation delayed. | Newsbytes |
| 36 | Plant City shooting kills five | Man kills wife and three children, then himself. | Times Now |
| 37 | UN expert welcomes ICJ verdict | Urges the world to stand with Rohingya survivors. | Scoop |
| 38 | UN: association needs no state OK | Human Rights Committee ruling. | Scoop |
| 39 | Kamala Harris meets Macron in Paris | Amid 2028 speculation. | Le Monde |
| 40 | US court limits Rollins' religious emails | Interim limits on the agriculture secretary's emails. | AppiSToS |

Markets strip: Nikkei −4.5% · KOSPI −4.7% · MSCI Asia −2.5% · SoftBank −12% · Dollar 159.8¥ — all reported on 20 November 2026 (CNA, Nikkei Asia, TradingView, Upstox).

## How the image was made

The v1 image (1024×1024, PNG, 183,576 bytes) was rendered programmatically with Python PIL from the 40 verified stories above. The layout is the same formula as the 11/18 v5 and 11/19 v1 front pages: nameplate + date, a big lead with a drawn scene (here, the market crash: skyline, falling chart, ticker tape), two second stories, a 12-item illustrated grid, a 25-item briefs section, a UTC timeline, and a markets strip. Every story was verified against reporting dated 20 November 2026 before it was drawn; no story was invented, and no headline was written from memory. The renderer refuses to finish (asserts) if any text would overlap, clip, or overflow its box.

## How to run it

```sh
python3 main.py            # writes entry.png to /output (or $MAKEFUN_OUTPUT_DIR)
python3 main.py /tmp/out   # writes entry.png to /tmp/out
```

`main.py` is Python 3.13 standard library only, makes no network calls, and copies the pre-rendered `entry.png`, so it is byte-identical on every run. To regenerate the image from the story data, run `python3 render_v1.py` (needs Pillow and the Liberation/DejaVu fonts).
