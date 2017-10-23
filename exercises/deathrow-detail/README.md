Death Row detail scraper
========================

Since we're on the subject of death row, check out [this project](https://apps.texastribune.org/death-row/) from the Texas Tribune, which basically puts a more reader-friendly interface on the [current list of inmates on Death Row in Texas](https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html).

Immediately seeing the faces, rather than a list of names, is pretty powerful. And the way the Tribune managed to get those was (you guessed it) writing a scraper.

This is a slightly more advanced scraping exercise, but it will set you up to more easily complete your scraping assignment when we hand it out later this week. If you guys can work through this, the assignment will be a little easier.

Objective
----------

Your objective is to implement a function called `get_image`, which — given the URL to a given inmate's [detail page](https://www.tdcj.state.tx.us/death_row/dr_info/colonejoseph.html) — will be able to retrieve the URL to [their image](https://www.tdcj.state.tx.us/death_row/dr_info/colonejoseph.jpg).

A few new things you'll be doing here:

  - Implementing a function. This is no different than regular code, except you'll be indenting it under the declaration of the `get_image` function at the top (this is clearly marked in the code).
  - Scraping info from something that isn't a table. Same rules apply.
  - Grabbing information from an HTML tag's attribute, rather than its text. There is an example of this in the code, or you can [Google](https://www.google.com/search?q=beautifulsoup+get+attribute&oq=beautifulsoup+get+attribute&aqs=chrome.0.0l6.31830j0j1&sourceid=chrome&ie=UTF-8) to find others.

Tips
----

  - Try running the program first. You'll see that it outputs the URL to each offender's detail page (I've written that part for you). Ultimately you want it to output the URL to the images.
  - Again, this is very, very similar to what you've already done. Don't overthink it.
  - Everything you need to do this is already in the code, but feel free to Google liberally.

Wrapping up
-----------

We'll discuss this on Wednesday. Good luck!