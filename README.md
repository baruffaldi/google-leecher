This software is intended to be used on all kinds of applications which needs to do some search on google and occasionally download its results.

It can be used on console as the most common applications or you can integrate it on your project.


---


# Console Usage #

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


---


# Integration #

If you set on constructor the query parameter the search will start automatically, otherwise you can start it by calling the method: search.

## Parameters ##

|query|your search keywords|
|:----|:-------------------|
|ext|choose the file extension to search|
|limit|limit to max N results (default:8)|
|start|set the search results offset (default:1)|
|download|download results|
|useragent|specify the user agent to use|
|recursive|get all results|

### Examples ###

```
Python 2.5 (release25-maint, Jul 20 2008, 20:47:25)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from googleleecher import GoogleLeecher
>>>
>>> gl = GoogleLeecher(query="test",ext="pdf")
>>>
>>> gl.done
True
>>>
>>> len(gl.results)
5
>>>
>>> for result in gl.results:
...   "%i %s" % ( gl.results.index(result), result["url"] )
...
'0 http://www.lsac.org/pdfs/test.pdf'
'1 http://testing.byu.edu/info/handbooks/betteritems.pdf'
'2 http://extension.oregonstate.edu/catalog/pdf/ec/ec1478.pdf'
'3 http://www.state.tn.us/education/assessment/doc/tsteststrategies.pdf'
'4 http://www.ets.org/Media/Tests/PRAXIS/pdf/01361anxiety.pdf'
>>>
>>> gl.results[1]
{'GsearchResultClass': 'GwebSearch', 'visibleUrl': 'testing.byu.edu',
'titleNoFormatting': 'How to Prepare Better Multiple-Choice Test Items: Guidelines for ...',
'title': 'How to Prepare Better Multiple-Choice \\u003cb\\u003eTest\\u003c/b\\u003e Items: Guidelines for
\\u003cb\\u003e...\\u003c/b\\u003e', 'url': 'http://testing.byu.edu/info/handbooks/betteritems.pdf',
'cacheUrl': 'http://www.google.com/search?q\\u003dcache:IH4LUypf0u8J:testing.byu.edu',
'unescapedUrl': 'http://testing.byu.edu/info/handbooks/betteritems.pdf',
'content': 'of the multiple-choice \\u003cb\\u003etest\\u003c/b\\u003e items used to assess student achievement.
\\u003cb\\u003e...\\u003c/b\\u003e   multiple-choice items to \\u003cb\\u003etest\\u003c/b\\u003e a broader
sample of course content in a given   amount \\u003cb\\u003e...\\u003c/b\\u003e'}
>>>
>>> gl.leech_result(1,"my-new-handbook.pdf")
True
>>>
>>> gl.leech_result(2)
%PDF-1.6\r%\xe2\xe3\xcf\xd3...
>>>
>>> data = gl.leech_result(0)
>>> fs = open("first-result.pdf","wb")
>>> fs.write(data)
>>> fs.close()
>>>
>>> len(open("first-result.pdf","r").read())
209610
```


---


# Win32 Port #

**Dependencies**:
  1. USER32.dll - C:\WINDOWS\system32\USER32.dll
  1. SHELL32.dll - C:\WINDOWS\system32\SHELL32.dll
  1. WSOCK32.dll - C:\WINDOWS\system32\WSOCK32.dll
  1. ADVAPI32.dll - C:\WINDOWS\system32\ADVAPI32.dll
  1. WS2\_32.dll - C:\WINDOWS\system32\WS2\_32.dll
  1. KERNEL32.dll - C:\WINDOWS\system32\KERNEL32.dll

**Compiling**

C:\python-path> python setup.py py2exe

# Future Implementations #

  * **Features**
    1. Support search channel switch ( images, books, etc, etc )
    1. When interactive mode, choose before download all files with a queue system
    1. Progress bar when downloading in console
    1. destination ( directory via console )( callback in python )

  * **Windows** Installer
    1. Check for dependencies

  * **Project** google-leecher-gui
    1. GUI written in python which uses this class


---


# Awards #

<a href='http://www.softpedia.com/progClean/Google-Leecher-Clean-154192.html' title='Softpedia Certificate'><img src='http://www.softpedia.com/base_img/softpedia_free_award_f.gif' alt='100% Free Software' /></a>


---


# Contributors #

At the moment, I'm alone.

**If you want to give your contribute to this project do not exitate to contact me and feel free to tell me everything you think about this class.**

A _right arm_ is always welcome ;)


---


# MIT License #

Copyright (c) 2009 Filippo Baruffaldi

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Google Leecher"), to deal in Google Leecher without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of Google Leecher, and to permit persons to whom Google
Leecher is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
