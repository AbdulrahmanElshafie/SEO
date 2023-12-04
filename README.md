# SEO V1

Ever wondered how some tools get the ranking for a specific keyword and measure ranking?
Or have you struggled with paid tools?

This project is aimed at helping SEO specialists with some of their tasks. This version is aimed at getting a ranking and doing some analysis on it.

All you have to do is:
1.  Enter the focus keywords you want to check the rankings for in the 'focus key phrases.txt' file, each word/term in a separate line 
2.  Run the app
3.  Enter the keyword you want to check its rank
4.  Watch the magic happen!

At the end of this program, you'll get some analysis of the search results.


In this project, I used the 'googlesearch' library, a library for searching Google, easily. 

After taking targeted keywords, we take each focus term and get the top n search results (currently set at 30) (top_n_serp function).

Then locate the targeted keyword in the results then save these results (locate_target function).

Sometimes you may get an error because too many requests were sent, to solve this issue we make the program sleep for some time and then try again, if this happens over 5 times the program will terminate automatically (rank).

To avoid starting again after this issue, we have a file called 'finished.txt', where we store the successful tries to don't lose our progress (save_results, add_to_finished, read_finished functions).

After the results are done you'll get some insights on it, like how many terms you rank in the top 10, 20, 30m, or not indexed and their percentage. Also, you'll have a sheet with each term and your rank for it. 



## Next Version
-  Getting the search results so you can do competitor research on the SERPs, and get some intuition about what your competitors do to rank on Google 
-  Take the required number of search results as input
-  Trying to solve the 'too many requests were sent error' in a more efficient way 
