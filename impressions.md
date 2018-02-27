- Agree with the point (p.7) that "the culture of mathematics and the culture of mathematics education are completely different"!
- I think it'd maybe be worth making the point in the intro that programmers will have probably encountered more mathematics
  than most, but that the issue is more of wanting to formalise this experience and establish rigor (that's how I see it anyway)
- This gap is quite difficult to bridge for self-taught mathematics, this kind of resource helps not consider it a worthless effort
- Not come across this cultural expectation that you write down examples for every definition, but think it'd have saved me time when
  working with varieties, when I eventually got to a point and realised I wasn't following the meaning of the text (not a great feeling!)
  - This is compared (on p.15) to writing tests, and in fairness I didn't write tests back then either...
- On the point made on p.17-18 that it's hard to "truly grok" linear algebra without seeing a matrix as a linear map, I agree and would
  add that what I found the most useful in 3B1B's videos wasn't so much the exposition (a video can't replace reading a full text imho)
  but a) presenting this dual interpretation and b) making the connection to computer graphics, playing around with which in Blender
  really helped make more intuitive to me. Additionally, not quite having clarified this made moving on to affine transformations
  so unintuitive as to be unreachable (and generally frustrating - still not sure how I'd fare if I tried again there but hope to retry).
- I'd also add that one thing that makes it hard to get into maths for programmers [including those studying not-maths at university] is
  not being able to see these threads of how things link together. One thing that I found useful was copying out a full maths syllabus,
  which seems to present a good idea of all the components a mathematician takes to get to where I'd like to be.
  - Notes on/links to Cambridge's _Mathematical Tripos_ syllabus here: https://git.io/vAkOP
- On p.40 (paragraph 2) you note the vertical pipe is used in place of the colon in set-builder notation sometimes - I may be wrong here,
  or it may just be for conditional probability, but I thought it was read as "given" (this may be insignificant, if so ignore)
- Did not know the subset operator could include equality!
- On p.42 (definition 8, para. 3) I think the book I read used 'there exists some' not 'there is some' (and this is more intuitive maybe?)
  but I don't know, maybe simplifying the language is the point here - again feel free to ignore
  - edit: on p.44 you refer to the symbol meaning "there exists", maybe worth making consistent so it's more easily recalled at this point
- On p.43 (definition 11), I think the notation `Im` for image hasn't been introduced? It was probably meant to go in definition 8 (?)
  - feels pedantic to point out (sorry!) but I did a double take since I'd not long been looking at Julia code for complex numbers
    where `Im` = imaginary, may be worth specifying explicitly
- On p.44 you note that injections are called 'one-to-one' in a footnote, not the main text, then later on p.44 you note that bijections are
  "also" called 'one-to-one' - I don't know if you'd disagree but I was a bit confused by the "also" before I got to the footnote, since
  it was the first time seeing this used [for bijections]. Just a thought, it makes sense once you get to the footnote obviously.
- I like how Tim Gowers links injection to the number of preimages an element has, not sure if that'd be helpful in this section
  - see: https://www.dpmms.cam.ac.uk/~wtg10/nasquestions.html
- The connection to cryptography for bijections on p.45 is a nice touch, thinking of the applied side helps reinforce.
  - It's harder to come up with similarly strong examples of sur/injections, perhaps including some of those too would be helpful?
  - edit: on p.55 you conclude the chapter that "bijections show up everywhere" so perhaps a lack of examples is the point
- On p.47 it might be nice to add a diagram for a double-cover? Also I'm a bit confused (probably I'm wrong here) but if the preimage `f^-1(Y)`
  for every `y` in `Y` has size 2 then set `Y` now includes the winner? Doesn't this contradict the function `f` defining "is lost by player"?
- On p.55 (4.6.1) maybe use the relative complement sign (`A\C`) rather than subtract (`A-C`) since the rest is introducing set theory symbols?
  - I found this example kind of hard to read, though I've used powersets in programming before and get the idea. I think it'd be helpful
    to explain it with some reference to the set {0,1} being equivalent to a Boolean, and thus interpretable as 'is a subset of'.
  - Having said this, it's still a little vague to me why this makes it a "power set" \[uniquely\] \(i.e. why not let the base = 3 (or what
    would the significance of this set of functions be?)
  - Wikipedia gives an explanation in terms of the indicator function (but doesn't name it as such), I found this very helpful to discover (but
    understand this may be more detail for an introductory book than you were aiming for, and maybe it's confusing to mention along with the
    functions of the powerset mapping)
  - Maybe break 4.6.1 into two parts - a) countable set b) power set - it was a bit confusing to me whether I was being asked to give an example
    of them together (i.e. of a countable power set)
- It'd be nice to know if I got the right answers to 4.6.4 (hopefully answers to exercises will be included?)
  - while working on 4.6.2 I came across Eggen et al. "A Transition to Advanced Mathematics", focused on proofs at UG level, seems like it's
    at the same level as this text [developed from a Central Michigan U. course]
- I can't follow 4.6.4 (I tried looking it up and am not sure if the Schröder–Bernstein theorem is what I need, it's not been introduced)
