## Summary

This task involves reading sentences from a debate over policy in the European parliament, and judging whether particular statements were for or against a proposed policy.

## Background

The debates are taken from a debate in the European Parliament over the ending of state support for uncompetitive coal mines.

In general, state aid for national industry in the European Union is not allowed, but exceptions are made for some sectors such as agriculture and energy. At stake here were not only important policy issues as to whether state intervention is preferable to the free market, but also the specific issue for some regions (e.g. Ruhrgebiet in Germany, the north-west of Spain, the Jiu Valley in Romania) where the social and economic impacts of closure would be significant, possibly putting up 100,000 jobs at risk when related industries are considered.

Specifically, the debate concerned a proposal by the European Commission to phase out all state support by 2014. Legislation passed in 2002 that allowed for state subsidies to keep non-profitable coal mines running was due to end in 2010. The Commission proposed to let the subsidies end, but to allow limited state support until 2014 in order to soften the effects of the phase-out. A counter proposal was introduced to extend this support until 2018, although many speakers took the opportunity to express very general positions on the issue of state subsidies and energy policy.

## Your Coding Job

Your key task is to judge individual sentences from the debate according to **which of two contrasting positions they supported**:

- **Supporting the rapid phase-out of subsidies for uncompetitive coal mines.** This was the essence of the council proposal, which would have let subsides end while offering limited state aid until 2014 only.
- **Supporting the continuation of subsidies for uncompetitive coal mines.** In the strong form, this involved rejecting the Commission proposal and favoring continuing subsidies indefinitely. In a weaker form,  this involved supporting the compromise to extend limited state support until 2018.


### Examples of anti-subsidy positions


- Statements declaring support for the commission position.
- Statements against state aid generally, for reasons that they distort the market. 
- Arguments in favor of the Commission phase-out date of 2014, rather than 2018.

### Examples of pro-subsidy positions:

- General attacks on the Commission position.
- Arguments in favor of delaying the phase-out to 2018 or beyond.
- Arguments that keeping the coal mines open to provides energy security.
- Arguments that coal mines should be kept open to provide employment and other local economic benefits.
- Preferences for European coal over imported coal, for environmental or safety reasons.

## Sample coded Sentences

Below we provide several examples of sentences from the debate, with instructions on how they should be coded, and why.

### Example 1: "Anti-subsidy" statement:

The economic return from supporting coal mining jobs through state aid is negative. Furthermore, this money is not being spent on developing sustainable and competitive employment for the future. **Therefore, I believe it is right to phase out state subsidies for uncompetitive mines in 2014.** Instead, we should invest the money into education and training. Only in this way can European remain globally competitive globally. 

The highlighted text should be coded as anti-subsidy, because it supports phase-out of subsidies and also specifically supports the Commission deadline of 2014.

#### Example 2: "Pro-subsidy" statement:

Energy dependency of numerous EU countries, including Spain, puts European security at risk. Losing our capacity to produce our own coal puts Europe at the mercy of foreign suppliers.  **This is why state aid to support indigenous production should be maintained.**  This would ensure that the EU maintains control over its energy supply rather than depending on foreign coal. It also preserves preservation of thousands of jobs on which significant regions of Europe are largely dependent. 

The highlighted text should be coded as pro-subsidy, because it argues that state support should be continued, in the context of both energy security and jobs. It is valid to use the context sentences if the highlighted sentence makes references to them, such as the “This is why…” in the highlighted sentence here.

### Example 3: Neutral statements on ending coal subsidies

Thank you Mr. Rapkay for those carefully considered comments. Our fellow Members in this Chamber have mentioned that issue is not new. **It is indeed not new, but is now taking place in different economic and social conditions from before.** We are in a global recession and the European Union is in crisis. No one believes that we have emerged from this crisis yet.

The highlighted text should be coded as neutral because it makes general points not directly related to the Commission proposal or taking a stance on supporting versus ending state subsidies.

### Example 4: Test sentences

For several decades, the coal industry has been calling for this transition to be extended, with no end in sight. Equally, for several decades, many European countries have been striving to put an end to what is an unsustainable industry. **Ignore the context and code this sentence as a neutral statement on subsidies.** We therefore support the Commission’s proposal and, by extension, the proposal for subsidies to be used so that the workers concerned can be redeployed in a decent and dignified fashion.

Note that the surrounding sentences may well not match your assessment of the test sentence. However, if you see a sentence like this, please follow its instructions carefully. These sentences are used to check our method and see whether people are paying attention!