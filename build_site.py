#!/usr/bin/env python3
"""Build the Sabri Suby — Quantum Growth swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/SABRI_SUBY_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {'SabriSuby_QGPower_VSL.mp4': 'The 24-minute Quantum Growth VSL. Wistia calls it &ldquo;4K USB HOOK v3&rdquo;.', 'SabriSuby_Algorithms Secret Sauce.mp4': 'Earlier asset from a prior capture.'}

CONFIG = {
 "SITE": "Sabri Suby — Quantum Growth",
 "CREATOR": "Sabri Suby",
 "ADS_KEY": "kingkong",
 "FUNNEL_IDS": ["F041"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/SABRI_SUBY_Swipe",
 "BLURB": "King Kong's agency funnel. Free training delivered <b>by SMS</b>, a 24-minute VSL, "
          "and a &ldquo;Growth Map&rdquo; call that is priced at $1,000 and then given away.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Brand","King Kong"),("Offer","Quantum Growth"),("VSL","24m 32s"),
           ("Wistia asset name","4K USB HOOK <b>v3</b>"),("Words","4,608"),
           ("CRM","Infusionsoft / Keap"),("Call framing","$1,000 strategy, free"),
           ("Price","never stated")],
 "OFFER": [("Product","Done-for-you agency growth &mdash; King Kong / Quantum Growth"),
   ("Lead magnet","Free training, <b>delivered by text message</b>, not email"),
   ("Call","&ldquo;Free 30-minute Growth Map call&rdquo;"),
   ("Anchor","The quiz CTA reads <b>&ldquo;GIVE ME THE $1,000 STRATEGY FOR FREE&rdquo;</b>"),
   ("Scarcity","&ldquo;As of Today <b>18th Of August</b>, all spots for this month are almost gone&rdquo; &mdash; the date is injected live"),
   ("Path","Opt-in (SMS) &rarr; VSL + timer &rarr; agency demo &rarr; quiz &rarr; strategy session"),
   ("Price","<b>Never stated</b> anywhere in the funnel or the 4,608-word VSL")],
 "FINDINGS": [
  ("They version their hooks, and the file name proves it",
   "The Wistia asset is titled <b>&ldquo;4K USB HOOK v3&rdquo;</b> &mdash; visible in the play "
   "button's accessible label. That is an internal name that leaked into production markup. It "
   "tells you the hook is a <i>tracked, versioned artefact</i> on at least its third iteration, "
   "and that the 4K/USB naming is their shorthand for a hook family. <b>We do not version our "
   "VSL hooks or name them.</b> They do, and it shows in the markup."),
  ("The date in the scarcity line is injected live",
   "The CTA read <i>&ldquo;Be Quick! As of Today <b>18th Of August</b>, All Spots For This Month "
   "Are Almost Gone!&rdquo;</i> on the day of capture. It is evergreen scarcity that never goes "
   "stale and never needs a human to update it. Costs one line of JS."),
  ("The free call is given a price before it is given away",
   "The quiz button says <b>GIVE ME THE $1,000 STRATEGY FOR FREE</b>. The call is anchored at "
   "$1,000 in the same breath it is made free, so the prospect books something valued rather "
   "than something cheap. Our class is &ldquo;free&rdquo; with no number attached to it."),
  ("The training is delivered by SMS, so the phone number is the real opt-in",
   "&ldquo;GET ACCESS NOW! <b>CHECK YA PHONE</b> AS WE'LL TEXT YOU THE TRAINING IMMEDIATELY&rdquo;. "
   "The deliverable is the reason to give a mobile number, and it makes the first text an "
   "<i>expected</i> one. Same problem Suprahuman and PB Trading solve differently."),
 ],
 "FUNNEL": [
  ("Opt-in","kingkong.co/quantum-growth","Free training, delivered by text. Infusionsoft form. Meta Pixel + GTM + GA."),
  ("VSL + timer","kingkong.co/qg-power",'<span class="tag good">the asset</span> Wistia &ldquo;4K USB HOOK v3&rdquo;, 24m32s. Live-dated scarcity line.'),
  ("Agency demo","kingkong.co/agency-demo","Second Wistia video, &ldquo;Agency Demo&rdquo;."),
  ("Quiz","kingkong.co/30-minute-strategy-session","3 growth levers. CTA anchors the call at $1,000."),
  ("Quiz confirmation","kingkong.co/qg-demo","Third video, &ldquo;QG Demo 2024&rdquo;."),
 ],
 "TRANSCRIPT_GROUPS": [("Quantum Growth VSL",[os.path.join(PKG,"Transcript/transcript.md")])],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>The most useful thing here is a file name.</b> Wistia exposes the VSL's
internal title, <b>&ldquo;4K USB HOOK v3&rdquo;</b>, in the player markup. It is proof that the
hook is treated as a versioned, iterated asset &mdash; not a thing you write once and ship.</div>

<h2 class="sec">Three ways this funnel prices a free thing</h2>
<div class="tablewrap"><table>
<tr><th>Element</th><th>What it does</th></tr>
<tr><td>&ldquo;GIVE ME THE <b>$1,000 STRATEGY</b> FOR FREE&rdquo;</td><td>Anchors the call's value before giving it away</td></tr>
<tr><td>&ldquo;Free 30-minute <b>Growth Map</b> call&rdquo;</td><td>Names the deliverable, so the call has an artefact</td></tr>
<tr><td>&ldquo;As of Today <b>18th Of August</b>&hellip;&rdquo;</td><td>Live-dated scarcity, no manual upkeep</td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> Our masterclass is free and named for
what it is. His is free and named for what you <i>leave with</i>. That is a rename, not a rebuild.</p>

<h2 class="sec">The stack</h2>
<p>Infusionsoft/Keap for every form, Wistia for every video, Meta Pixel + GTM + GA throughout.
Notably <b>no Hyros</b> &mdash; unusual for an agency at this spend level, and worth contrasting
with PB Trading, Brez Scales and Dlucs, who all run it.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>No price</b> in 4,608 words or on any page.</li>
<li><b>No emails.</b> The opt-in was never submitted &mdash; and note the deliverable is an SMS, so
an email capture alone would not have got the sequence.</li>
<li><b>The agency demo and QG Demo 2024 videos are identified but not pulled.</b></li></ul>
""",
}
CONFIG["VIDEOS"] = video_library()

if __name__ == "__main__":
    build(CONFIG)
