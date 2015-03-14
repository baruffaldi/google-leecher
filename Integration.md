# Introduction #

If you set on constructor the query parameter the search will start automatically, otherwise you can start it by calling the method: search.

# Details #

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