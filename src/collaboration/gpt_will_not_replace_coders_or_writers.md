### GPT won't replace us, but it will make us better communicators

The unforeseen benefit of GPT algorithms is not additive, it's [subtractive](https://www.nature.com/articles/s41586-021-03380-y).

Like you, I've been reading the hype about how GPT has weaponized NLP and is going to be [the beginning of the end](https://kitze.io/posts/gpt3-is-the-beginning-of-the-end) of pretty much everything we know and love from [programming](https://www.wired.com/story/openai-copilot-autocomplete-for-code/) to [writing](https://www.theatlantic.com/technology/archive/2022/09/artificial-intelligence-machine-learing-natural-language-processing/661401/). 

While being blown away by some of the quick and seemingly transcendent results that I got from my early experiments with GPT-3, after studying this closely for a while, I realized that what I had seen when I initially described it as magic, was actually a result of starting with the text of an exceptional writer and that text being large enough for the machine to sound like the author without using the author's words verbatim. 

That is, unless you actually are Byung Chul Han, what you'll get back from GPT-3 is likely less than perfect copy-pasta that sounds a bit uncanny valley. It's a stop along the editing road. I should know, I actually ran GPT-3 through small corpora of text from Han and what I got back was as resplendent as what I had read from Han without being quite as deep or difficult to unpack.

All else being equal, the smaller the input corpus, the more GPT-3 is just copy-pasta. Where it really shines is when the input corpus is large and the author is a professional. Then the output sounds like the author without plagiarizing a single word. I'm not sure where the threshold is but it's likely similar to the limits on measuring readability metrics.

It's as if you handed a Han book to your junior copywriter and asked for an abstract. There's actually good value proposition in the traditional academic publishing sense of a Han Reader, but that's beyond the scope of this discussion.

My stated personal goal was always that I admired the aphorisms of Nietzsche or Szasz but given my ramble-on, stream-of-consciousness writing style, I didn't really want to bring a premature end to the joy I get from writing fast and furious by having automagical transforms. 

GPT-3 is actually quite useful for getting a quick summary or tldr to remove cruft, the kind of sideways writing that's my default mode and takes enormous effort to tighten manually even for an experienced editor. 

There, the value proposition is priceless since we have little way of reducing the stack overflow that our brains face daily as the breadth and depth of information complexity overwhelms even the smartest among us.

So, with that idea in mind, I did the following experiment. I started with [paragraphs of recommendations that colleagues have written on linkedin as input](https://www.linkedin.com/in/davidthewatson/details/recommendations/?profileUrn=urn%253Ali%253Afsd_profile%253AACoAAAAXcOEBi-yauHTCxj3C7DCSjyXqWa7Zqkw&tabIndex=0&detailScreenTabIndex=0). Then I took the output from [my spin on a recursive summarizer script](https://github.com/davidthewatson/recursive_summarizer) on github using GPT-3:

    ╭─watson@acer in repo: recursive_summarizer on  main [!] via  v3.10.8 (.venv) took 25s
    ╰─λ python recursively_summarize.py

    word count:	 335

    1 of 2  -  David Watson is an excellent engineer with a rare ability to see the big picture and pay attention to detail. He is also a great listener and has a genuine interest in helping others achieve their goals. His vast knowledge and experience make him a valuable asset to any team, and his drumming skills are an added bonus!

    2 of 2  -  David Watson is a renaissance man who has dedicated his life to pursuing knowledge and understanding in a variety of disciplines. He is a man of many talents and skills, and he has a passion for learning. He is a true renaissance man!

And used that as input to my final human editing stage to produce the final output which you can find [here](/other/quotes.txt).

Since the English language presents a choice paradox for writers and speakers alike, it's obvious that less is more when it comes to editing aphorisms. This in spite of the fact that the book's subtitle was more is less. Schwarz was referring to products, of course, not words in a dictionary.

Quantitatively, you can see how this works:

    ╭─watson@acer in ~ took 1ms
    ╰─λ wc *.txt
    6  337 2026 1st.txt
    3  109  583 2nd.txt
    3   48  300 3rd.txt
    12  494 2909 total

We go from the linkedin version with 337 words to the version returned from GPT-3 at 109 words - almost exactly 1/3 to the final human-edited version with a 45% reduction from the GPT version but only 14% of the original! There's a reason so many authors refer to this as a kind of automated tldr; or abstract. I'm not sure how long this will take to reach humanities programs but it's probably de rigueur for computer science programs.

The qualitative statistics like Flesch-Kincaid and the like are not as dramatic but do show an improvement of about a grade level per step in my 3-step experiment.

I'm satisfied with the result given the work I put into exploring GPT this summer. I'm sure it's nowhere near [where Notion AI is now](https://www.notion.so/blog/introducing-notion-ai) but the future is promising for those of us who can write, but are challenged in the reductionist editing process. 

