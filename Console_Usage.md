# Introduction #

.


# Details #

```
03:53:21 bornslippy@oxygen:~$ ./g-leecher.py
Google Results Leecher v0.4
--------------------------
[*][U] This version is up to date.
syntax: g-leecher.py [options] your search terms
             --help | -h        - this usage screen
         --download | -d        - download results
            --force | -f        - disable interactive mode
        --recursive | -r        - get all results
 --useragent=string | -u=Moz... - specify the user agent to use
        --limit=int | -l=8      - limit to max N results (default:8)
        --start=int | -s=1      - set the search results offset (default:1)
       --ext=string | -e=pdf    - choose the file extension to search

example: g-leecher.py -d good hotdogs
03:53:28 bornslippy@oxygen:~$
```

### Example ###

```
03:53:28 bornslippy@oxygen:~$ ./g-leecher.py -d good hotdogs
Google Results Leecher v0.4
--------------------------
[*][U] This version is up to date.
[**] Searching for: good hotdogs
[**] 8 files found:
[-] YouTube - Hot Dogs are Good
[-] Red Hot Chicago - A Chicago Style Hot Dog Since 1893
[-] Which hot dogs are the tastiest? - By Ben Wasserstein - Slate Magazine
[-] Hot Doug\u0026#39;s in Chicago: Good Hot Dogs and Good Neighbors in Line ...
[-] Good Hotdog like Grey\u0026#39;s Papaya? - Washington DC \u0026amp; Baltimore Area ...
[-] Good hotdog places (Raleigh, Durham, Chapel Hill: chapel, houses ...
[-] The man who sold very good hotdogs
[-] Food Science: GOOD Hot Dogs, wellness coach, hot dogs
[**] let's leech...
[?] Download 'YouTube - Hot Dogs are Good'? (default: No) [Y]es [N]o [A]ll [S]top: Y
[+] Saving 'YouTube - Hot Dogs are Good' as 'watch3Fv3DKlNPf9cNGI.html'
[?] Download 'Red Hot Chicago - A Chicago Style Hot Dog Since 1893'? (default: No) [Y]es [N]o [A]ll [S]top: N
[?] Download 'Which hot dogs are the tastiest? - By Ben Wasserstein - Slate Magazine'? (default: No) [Y]es [N]o [A]ll [S]top:
[?] Download 'Hot Doug\u0026#39;s in Chicago: Good Hot Dogs and Good Neighbors in Line ...'? (default: No) [Y]es [N]o [A]ll [S]top: A
[+] Saving 'Hot Doug\u0026#39;s in Chicago: Good Hot Dogs and Good Neighbors in Line ...' as '200910.html'
[+] Saving 'Good Hotdog like Grey\u0026#39;s Papaya? - Washington DC \u0026amp; Baltimore Area ...' as 'topics650640.html'
[+] Saving 'Good hotdog places (Raleigh, Durham, Chapel Hill: chapel, houses ...' as 'forum.html'
[+] Saving 'The man who sold very good hotdogs' as 'storiesattitude.html'
[+] Saving 'Food Science: GOOD Hot Dogs, wellness coach, hot dogs' as 'q.html'
[**] Done!
04:10:04 bornslippy@oxygen:~$
```