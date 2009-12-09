#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2, urllib, getopt, sys, os, UserDict
reload(sys)
sys.setdefaultencoding('utf-8')
#
# Google Leecher
#
# Copyright (c) 2009 Filippo Baruffaldi
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files ("Google Leecher"), to deal in Google Leecher without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of Google Leecher, and to permit persons to whom Google 
# Leecher is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

"""
This software is intended to be used on all kinds of applications which
needs to do some search on google and occasionally download its results.

It can be used on console as the most common applications or you can
integrate it on your project.

@author: Filippo Baruffaldi
@contact: filippo@baruffaldi.info
@copyright: some rights reserved
@license: MIT License
@organization: CoolMinds Developers Network
@version: 0.4.3
@todo: check gdata response encoding
"""

__author__ = "Filippo Baruffaldi"
__version__ = "0.4.3"

DEFAULT_USERAGENT = 'Google Leecher (+http://code.google.com/p/google-leecher)'
UPDATES_URL = "http://google-leecher.googlecode.com/files/latest.txt"
G_DATA_API_URL = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&start=%s&rsz=large'

class GoogleLeecher(object):
  query = ""
  ext = ""
  useragent = ""
  download = False
  download_all = False
  recursive = False
  limit = 8
  start = 1
  results = []
  failed_entries = []
  done = False
  force = False
    
  """
  Here we set every option override on constructor and let the
  search starts if a query has been specified
  
  @param query: [string] your search terms
  @param ext: [string] choose the file extension to search
  @param limit: [int] limit to max N results
  @param start: [int] set the search results offset
  @param download: [bool] download results
  @param useragent: [string] specify the user agent to use
  @param recursive: [bool] get all results
  """
  def __init__(self, query=False,ext=False,limit=False,start=False,\
                             download=False,useragent=False,recursive=False,force=False):
    if limit:
      self.limit = limit
    if start:
      self.start = start
    if download:
      self.download = download
    if useragent:
      self.useragent = useragent
    if recursive:
      self.recursive = recursive
    if __name__ == "__main__":
      self.force = force
    else:
      self.force = True
    if ext:
      self.ext = ext
    if query:
      self.query = query
      self.search()
    
  """
  This method try to leech a plain/text file which
  contain the current published version
  
  @return: int - if was impossible to check
  @return: bool - no new version found
  @return: string(version) - if newer version is found
  """
  def check_for_updates(self):
    current_version = self.leech(UPDATES_URL)
    if not current_version:
      return -1
    if current_version > __version__:
      return current_version
    else: return False
    
  """
  This method handles the google queries and doing it
  recursively if requested
  """
  def search(self):
    if self.recursive and self.limit != 8:
        while self.start < self.limit:
            self.results += self.query_google()
        self.done = True
    elif self.recursive:
        while not self.done:
            self.results += self.query_google()
    else:
        self.results = self.query_google()
        self.done = True

  """
  This method estabilish a connection to the json google data
  api in order to get the search results
  
  @return: list - the results
  """
  def query_google(self):
    self.query = urllib.quote("%s ext:%s" % (self.query, self.ext)) if self.ext else urllib.quote(self.query)
 
    url = G_DATA_API_URL % (self.query, self.start)

    try:
      req = urllib2.Request(url)
      opener = urllib2.build_opener()
      data_string = opener.open(req).read()
  
    except urllib2.URLError:
      return False

    # let's decode the json google answer
    data = []
    data_string = data_string.replace(": null,", ": None,")
    exec("data = " + data_string)

    # we don't like long names
    self.start += 8
    if len(data["responseData"]["results"]):
        self.results += data["responseData"]["results"] if self.start < self.limit\
            else data["responseData"]["results"][:(9-(self.start - self.limit))]
    else:
        self.done = True

    return self.results
    
  """
  This method simply download a file of a specific URL
  
  @param url: [string] the location of the file to download
  @param filename: [string] the filename to use if you want to automatically save it
  @return: bool - download result
  @return: stream - if no one filename specified
  """
  def leech(self, url, filename=False):
    if not self.useragent:
      self.useragent = 'Google Leecher (+http://code.google.com/p/google-leecher)'
    if filename:
      try:
        req = urllib2.Request(url, None, { 'User-Agent' : self.useragent })
        fs = open(filename, 'wb')
        fs.write(urllib2.urlopen(req).read())
        fs.close()
        return True
      except:
        if url in self.results:
          self.failed_entries.append(filename)
        return False
    else:
      try:
        req = urllib2.Request(url, None, { 'User-Agent' : self.useragent })
        return urllib2.urlopen(req).read()
      except:
        if url in self.results:
          self.failed_entries.append(filename)
        return False

  """
  This method download a specific results entry.
  If no one filename is specified it will return the entries streams.

  @param index: [int] the result number
  @param filename: [string] the filename to use if you want to automatically save it  
  @return: string - if single content are requested
  @return: list - if multiple content are requested
  """
  def leech_result(self, index, filename=False):
    if not self.useragent:
      self.useragent = DEFAULT_USERAGENT

    if isinstance(index, list) == "list":
      return [self.leech(self.results[i]["url"]) for i in index]
      
    if index < 0 or index > self.results.__len__():
      return None
    
    return self.leech(self.results[index]["url"], filename)

  """
  This method is used if there are no arguments when called
  from the console
  
  @note: Console method
  """
  def usage(self):
    print "syntax: %s [options] your search terms" % sys.argv[0].split("\\")[-1]
    print "             --help | -h        - this usage screen"
    print "         --download | -d        - download results"
    print "            --force | -f        - disable interactive mode"
    print "        --recursive | -r        - get all results"
    print " --useragent=string | -u=Moz... - specify the user agent to use"
    print "        --limit=int | -l=%i      - limit to max N results (default:%i)"  % ( self.limit, self.limit )
    print "        --start=int | -s=%i      - set the search results offset (default:%i)" %  ( self.start, self.start )
    print "       --ext=string | -e=pdf    - choose the file extension to search"
    print
    print "example: %s -d good hotdogs" % sys.argv[0]  

  """
  This method handles the console capabilities and workflow
  
  @note: Console method
  """
  def console(self):
    current_version = self.check_for_updates()
    if current_version:
      print "[U] Update available!!!"
      print "[U][+] Your version: %s" % __version__
      print "[U][+] Version available: %s" % current_version
      print "[U][+] Download it at http://google-leecher.googlecode.com"
    elif current_version == -1:
      print "[x] Error while checking for updates! Check your internet connection and retry later..."
    else: print "[U] This version is up to date."
    
    self.getopt(sys.argv)

    print "[**] Searching for: %s" % self.query

    self.search()
    
    if False in self.results and not self.done:
      print "[XXX] Google API connection failed."
      return

    print "[**] %i files found:" % self.results.__len__()

    urls = []
    titles = []
    for i in self.results:
      """collect target urls and titles"""
      print "[-] %s" % i["titleNoFormatting"]
      titles.append(i["titleNoFormatting"])
      urls.append(i["url"])
      
    if self.download:
      print "[**] let's leech..."
      
      for url in urls:
        result = True
        if len(url.split('/')) == 4:
            filename = url.split('/').pop()
        else: filename =  url.split('/')[2:]
        if filename == '':
            filename = "".join([x for x in url if x.isalpha() or x.isdigit() or x == '.'])
        filename = "".join([x for x in filename if x.isalpha() or x.isdigit() or x == '.'])
        
        if not self.ext: self.ext = "html"
        
        if filename[len(filename)-4:].lower() != '.%s' %self.ext:
            filename += '.%s' % self.ext
        
        if not filename:
          filename = "untitled"
        
        while(os.path.exists(filename)):
            filename = "%i-%s" % (urls.index(url),filename)
        
        if self.download_all:
          result = self.leech(url, filename, titles[urls.index(url)])
          print "[+] Saving '%s' as '%s'" % (titles[urls.index(url)],filename)
          
        else:
          action = str(self.ask_for_action(titles[urls.index(url)])).upper()
          if action == "S":
            print "[*] Quitting..."
            return
          
          if action == "A":
            self.download_all = True
            
          if action == "Y" or action == "A":
            result = self.leech(url, filename, titles[urls.index(url)])
        
        if not result:
          print "[x] Error while saving %s!" % filename

      if self.failed_entries:
          ret = ""
          for e in self.failed_entries:
              ret += "%s " % e
              
          print "[XXX] Done, but %i files wasn't been leeched: %s" % (len(self.failed_entries), ret)
          return

    print "[**] Done!"

  """
  This method parse the arguments, validate it and make
  it available to the application console workflow
  
  @param argv: [list] the arguments to parse
  @note: Console method
  """
  def getopt(self, argv):
    if not argv[1:].__len__():
        """we need something to search"""
        self.usage()
        sys.exit()
        
    try:
      opts, args = getopt.getopt(argv[1:], "hfdreslu",
                                 ["help", "force", "download", "recursive", "ext=", "start=", "limit=", "useragent="])
      
    except getopt.GetoptError, err:
      self.usage()
      print
      print "[XXX] %s" % str(err)
      sys.exit(2)
      
    for opt, arg in opts:
      """process the arguments"""
      if opt in ("-h", "help"):
        self.usage()
        sys.exit()
      elif opt in ("-e", "--ext"):
        self.ext = arg
      elif opt in ("-s", "--start"):
        self.start = int(arg)
      elif opt in ("-f", "--force"):
        self.download = True
        self.download_all = True
      elif opt in ("-l", "--limit"):
        self.limit = int(arg)
      elif opt in ("-d", "--download"):
        self.download = True
      elif opt in ("-r", "--recursive"):
        self.recursive = True
      elif opt in ( "-u", "--useragent"):
        self.useragent = str(arg)
    
    for keyword in args:
      """getting the keywords to search"""
      self.query += "%s " % keyword

  """
  This method asks to the user which one action we have to take
  
  @note: Console method
  @return: string ( the user choice )
  """
  def ask_for_action(self, title):
    return raw_input("[?] Download '%s'? (default: No) [Y]es [N]o [A]ll [S]top: " % title if title else"untitled" )
  
if __name__ == "__main__":
  print "Google Results Leecher v%s" % __version__
  print "--------------------------"
  GoogleLeecher().console()
  