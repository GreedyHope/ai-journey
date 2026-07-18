# AI Journey

Learning AI in public. No degree, no classroom — just building.

## Log

* Day 1: Repo created. Starting with Python basics + first project idea: \_\_\_
* Day 1 complete: Built a command-line AI tool from scratch. Switched providers mid-build (Anthropic → Gemini) due to billing. Added a custom personality via system prompts. Debugged model deprecations, env variable issues, and git setup along the way.
* Day 2: Added conversation memory using a running history list. Learned that context only persists within a single script run, not across restarts — sets up tomorrow's lesson on persistent memory (saving to a file).
* Day 3: Added persistent memory - conversations now save to memory.json and reload on restart. Confirmed it survives full program restarts, not just single sessions. Excluded memory.json from git so personal chat history stays private. Learned this is the same core pattern real chat apps use to remember users across sessions.
* Day 4: Added document Q\&A. The script reads notes.txt and grounds its answers in that content. Confirmed it correctly refuses to answer when the info isn't in the document, rather than guessing - good hallucination resistance.

