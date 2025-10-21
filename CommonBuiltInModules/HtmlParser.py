# 解析html页面
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html class="js no-touch geolocation fontface generatedcontent svg formvalidation placeholder boxsizing no-retina" lang="en" dir="ltr" style=""><!--<![endif]--><head>
    <script type="text/javascript" async="" src="https://ssl.google-analytics.com/ga.js"></script><script defer="" data-domain="python.org" src="https://analytics.python.org/js/script.outbound-links.js"></script>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script async="" src="https://media.ethicalads.io/media/client/v1.4.0/ethicalads.min.js" integrity="sha256-U3hKDidudIaxBDEzwGJApJgPEf2mWk6cfMWghrAa6i0= sha384-UcmsCqcNRSLW/dV3Lo1oCi2/VaurXbib6p4HyUEOeIa/4OpsrnucrugAefzVZJfI sha512-q4t1L4xEjGV2R4hzqCa41P8jrgFUS8xTb8rdNv4FGvw7FpydVj/kkxBJHOiaoxHa8olCcx1Slk9K+3sNbsM4ug==" crossorigin="anonymous"></script>
    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.08a078d0aa02.css" rel="stylesheet" type="text/css" media="all" title="default">
    <link href="/static/stylesheets/mq.98d6092b2ada.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty">
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen">
    

    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.bf0c425cdb73.css" rel="stylesheet" type="text/css" media="screen" />
    
    
    <![endif]-->
    <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">

    
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">

    
    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Our Events | Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">

    
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Our Events">
    <meta property="og:description" content="The official home of the Python Programming Language">
    
    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">
    
    <meta property="og:url" content="https://www.python.org/events/python-events/">

    <link rel="author" href="/humans.txt">

    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals" href="https://peps.python.org/peps.rss">
    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities" href="https://www.python.org/jobs/feed/rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News" href="https://pyfound.blogspot.com/feeds/posts/default?alt=rss">
    <link rel="alternate" type="application/rss+xml" title="Python Insider" href="https://blog.python.org/feeds/posts/default?alt=rss">
   <link rel="alternate" type="application/rss+xml" title="Python Releases" href="https://www.python.org/downloads/feed.rss">

    

    
    <script type="application/ld+json">
     {
       "@context": "https://schema.org",
       "@type": "WebSite",
       "url": "https://www.python.org/",
       "potentialAction": {
         "@type": "SearchAction",
         "target": "https://www.python.org/search/?q={search_term_string}",
         "query-input": "required name=search_term_string"
       }
     }
    </script>

    
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-39055973-1']);
    _gaq.push(['_trackPageview']);

    (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
    
<style type="text/css">#_copy{align-items:center;background:#4494d5;border-radius:3px;color:#fff;cursor:pointer;display:flex;font-size:13px;height:30px;justify-content:center;position:absolute;width:60px;z-index:1000}#select-tooltip,#sfModal,.modal-backdrop,div[id^=reader-helper]{display:none!important}.modal-open{overflow:auto!important}._sf_adjust_body{padding-right:0!important}.enable_copy_btns_div{position:fixed;width:154px;left:10px;top:45%;background:#e7f1ff;border:2px solid #4595d5;font-weight:600;border-radius:2px;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Helvetica Neue,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;z-index:5000}.enable_copy_btns_logo{width:100%;background:#4595d5;text-align:center;font-size:12px;color:#e7f1ff;line-height:30px;height:30px}.enable_copy_btns_btn{display:block;width:128px;height:28px;background:#7f5711;border-radius:4px;color:#fff;font-size:12px;border:0;outline:0;margin:8px auto;font-weight:700;cursor:pointer;opacity:.9}.enable_copy_btns_btn:hover{opacity:.8}.enable_copy_btns_btn:active{opacity:1}</style><style>.Po4BvhR1CK2tJaywJ6AN path {
  fill: var(--icon-path-fill);
}
.Oz4yDjua3Qe6thqkZYf_ path {
  transition: 0.2s all;
}
.Oz4yDjua3Qe6thqkZYf_:hover path {
  fill: var(--icon-hover-fill);
}
</style><style>/* ！！！切勿直接改动该文件，该文件由 generator.ts 自动生成！！！ */
/* !!! DONT MODIFY THIS FILE DIRECTLY, THIS FILE IS GENERATED BY generator.ts AUTOMATICALLY !!! */
.ibW4Oa5B7s2zJKKZ4pCg {
  user-select: none;
}
.AtqKyJetjrG4smuk35Np {
  max-width: 346px;
  width: auto;
  height: 36px;
  background-color: var(--quark-style-white-color, #fff);
  padding-left: 10px;
  padding-right: 4px;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  border: 1px solid var(--quark-style-gray-20-color, rgba(6, 10, 38, 0.12));
  box-shadow: 0 12px 32px -6px var(--quark-style-gray-30-fixed-color, rgba(6, 10, 38, 0.24));
  border-radius: 10px;
}
.ibW4Oa5B7s2zJKKZ4pCg .g6iGsZa_KHMeW2yICzQQ {
  height: 28px;
  display: flex;
  align-items: center;
  margin-right: 6px;
}
.ibW4Oa5B7s2zJKKZ4pCg .e4UXx38MPgfHdym_Lzt0 {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  height: 28px;
  padding: 0 6px;
  margin-right: 2px;
  border-radius: 6px;
  column-gap: 4px;
}
.ibW4Oa5B7s2zJKKZ4pCg .e4UXx38MPgfHdym_Lzt0:hover:not(.ibW4Oa5B7s2zJKKZ4pCg .kNOcXLDT_cCrcoY8LTm8) {
  background: var(--quark-style-gray-10-color, rgba(6, 10, 38, 0.06));
}
.ibW4Oa5B7s2zJKKZ4pCg .kNOcXLDT_cCrcoY8LTm8 {
  cursor: default;
}
.ibW4Oa5B7s2zJKKZ4pCg .kNOcXLDT_cCrcoY8LTm8 .Va3czASiR9Zztyl_lD4M {
  color: var(--quark-style-gray-40-color, rgba(6, 10, 38, 0.4)) !important;
}
.ibW4Oa5B7s2zJKKZ4pCg .e4UXx38MPgfHdym_Lzt0 .Va3czASiR9Zztyl_lD4M {
  font-size: 12px;
  color: var(--quark-style-gray-color, #060A26);
  line-height: 16px;
  white-space: nowrap;
  position: relative;
}
.ibW4Oa5B7s2zJKKZ4pCg .llw0qsmiI_08u93bFdNg {
  position: relative;
  width: 28px;
  height: 28px;
  overflow: visible !important;
}
.ibW4Oa5B7s2zJKKZ4pCg .LEo8kpqIERehkv8AhAfG {
  width: 28px;
  height: 28px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border-radius: 6px;
  overflow: visible !important;
}
.ibW4Oa5B7s2zJKKZ4pCg .LEo8kpqIERehkv8AhAfG:hover {
  background: var(--quark-style-gray-10-color, rgba(6, 10, 38, 0.06));
}
.ibW4Oa5B7s2zJKKZ4pCg .zoNmooxAnbLEJSN8m1Jg {
  box-sizing: border-box;
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 110px;
  max-height: 136px;
  height: auto;
  top: 36px;
  right: -5px;
  padding: 4px 0;
  background-color: var(--quark-style-white-color, #fff);
  border: 1px solid var(--quark-style-gray-20-color, rgba(6, 10, 38, 0.12));
  box-shadow: 0 4px 16px -6px var(--quark-style-gray-20-fixed-color, rgba(6, 10, 38, 0.12));
  border-radius: 8px;
  overflow: visible !important;
  row-gap: 4px;
}
.ibW4Oa5B7s2zJKKZ4pCg .O1imPofna4elG_8NcQnR {
  top: -77px;
}
.ibW4Oa5B7s2zJKKZ4pCg .mdH0IY7jS3Swn5vdX6tz {
  width: 102px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  cursor: pointer;
  column-gap: 8px;
  border-radius: 6px;
  padding: 0 6px;
  box-sizing: border-box;
}
.ibW4Oa5B7s2zJKKZ4pCg .mdH0IY7jS3Swn5vdX6tz:hover:not(.ibW4Oa5B7s2zJKKZ4pCg .dEdHLVmn_L2GAzb_cmwt) {
  background: var(--quark-style-gray-10-color, rgba(6, 10, 38, 0.06));
}
.ibW4Oa5B7s2zJKKZ4pCg .dEdHLVmn_L2GAzb_cmwt {
  cursor: default;
}
.ibW4Oa5B7s2zJKKZ4pCg .dEdHLVmn_L2GAzb_cmwt .zEraruudgjR2MToGu4Kw {
  color: var(--quark-style-gray-40-color, rgba(6, 10, 38, 0.4)) !important;
}
.ibW4Oa5B7s2zJKKZ4pCg .XfCMwvO0DsqFCeyzPYP2 {
  width: 16px;
  height: 16px;
}
.ibW4Oa5B7s2zJKKZ4pCg .zEraruudgjR2MToGu4Kw {
  font-size: 12px;
  color: var(--quark-style-gray-color, #060A26);
}
.ibW4Oa5B7s2zJKKZ4pCg .KZeoAuXbMIkWzOT4PcH5 {
  width: 100%;
  height: 1px;
  background: var(--quark-style-gray-10-color, rgba(6, 10, 38, 0.06));
}
.ZL32C_XdLL8UQRZ3zObd {
  display: flex;
  align-items: center;
}
.u5llx7cIQZLdrjP5Vag1 {
  width: 28px;
  height: 28px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 16px;
  cursor: pointer;
  margin-right: 12px;
  background: var(--quark-style-gray-60-color, rgba(6, 10, 38, 0.6));
}
.ZL32C_XdLL8UQRZ3zObd .LEo8kpqIERehkv8AhAfG {
  border-radius: 16px !important;
  background: var(--quark-style-gray-60-color, rgba(6, 10, 38, 0.6)) !important;
}
.ZL32C_XdLL8UQRZ3zObd .zoNmooxAnbLEJSN8m1Jg {
  right: 0 !important;
}
.ZL32C_XdLL8UQRZ3zObd {
  overflow: visible !important;
}
</style></head>

<body class="python events default-page" inmaintabuse="1">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While JavaScript is not essential for this website, your interaction with the content will be limited. Please turn JavaScript on for the full experience. </p>
        </div>

        <!--[if lte IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p>
                <strong>Notice:</strong> Your browser is <em>ancient</em>. Please
                <a href="http://browsehappy.com/">upgrade to a different browser</a> to experience a better web.
            </p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">

                
                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>

                
                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>▼</span></span> Close
                </a>

                

<ul class="menu" role="tree">
    
    <li class="python-meta current_branch selected">
        <a href="/" title="The Python Programming Language" class="current_branch selected">Python</a>
    </li>
    
    <li class="psf-meta ">
        <a href="https://www.python.org/psf/" title="The Python Software Foundation">PSF</a>
    </li>
    
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation">Docs</a>
    </li>
    
    <li class="pypi-meta ">
        <a href="https://pypi.org/" title="Python Package Index">PyPI</a>
    </li>
    
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board">Jobs</a>
    </li>
    
    <li class="shop-meta ">
        <a href="/community/">Community</a>
    </li>
    
</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python™"></a>
                </h1>

                <div class="options-bar-container do-not-print">
                    <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&amp;id=2" class="donate-button">Donate</a>
                    <div class="options-bar">
                        
                        <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">≡</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                            <fieldset title="Search Python.org">

                                <span aria-hidden="true" class="icon-search"></span>

                                <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                                <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                    GO
                                </button>

                                
                                <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                            </fieldset>
                        </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                            <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                                <li class="tier-1 last" aria-haspopup="true">
                                    <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                    <ul class="subnav menu">
                                        <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                        <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                        <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div><div class="winkwink-nudgenudge">
                            <ul class="navigation menu" aria-label="Social Media Navigation">
                                <li class="tier-1 last" aria-haspopup="true">
                                    <a href="#" class="action-trigger">Socialize</a>
                                    <ul class="subnav menu">
                                        <li class="tier-2 element-1" role="treeitem"><a href="https://www.linkedin.com/company/python-software-foundation/"><i aria-hidden="true" class="fa fa-linkedin-square"></i>LinkedIn</a></li>
                                        <li class="tier-2 element-2" role="treeitem"><a href="https://fosstodon.org/@ThePSF"><span aria-hidden="true" class="icon-mastodon"></span>Mastodon</a></li>
                                        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                        <li class="tier-2 element-4" role="treeitem"><a href="https://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                        <span data-html-include="/authenticated"><div class="account-signin">
    <ul class="navigation menu" aria-label="Social Media Navigation">
        <li class="tier-1 last" aria-haspopup="true">
            
            <a href="/accounts/login/" title="Sign Up or Sign In to Python.org">Sign In</a>
            <ul class="subnav menu">
                <li class="tier-2 element-1" role="treeitem"><a href="/accounts/signup/">Sign Up / Register</a></li>
                <li class="tier-2 element-2" role="treeitem"><a href="/accounts/login/">Sign In</a></li>
            </ul>
            
        </li>
    </ul>
</div>

</span>
                    </div><!-- end options-bar -->
                </div>

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">
                    
                        
<ul class="navigation menu" role="menubar" aria-label="Main Navigation">
  
    
    
    <li id="about" class="tier-1 element-1   with-supernav" aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
<li class="tier-2 super-navigation">
                                <h4>Python is a programming language that lets you work more quickly and integrate your systems more effectively.</h4>
                                <p>You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.  <a href="/about">Learn more about Python</a>.
                            </p></li></ul>

        
    </li>
    
    
    
    <li id="downloads" class="tier-1 element-2   with-supernav" aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/downloads/android/" title="">Android</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
<!-- Download supernav from templates/downloads/supernav.html - Last updated at Oct. 9, 2025, 8:41 p.m. -->
<li class="tier-2 super-navigation">
    
    <div class="download-os-source" style="display: none;">
        
        <h3>Python Source</h3>
        

        
        <p>
            <a class="button" href="https://www.python.org/ftp/python/3.14.0/Python-3.14.0.tar.xz">Python 3.14.0</a>
        </p>
        
        
        <p>Not the OS you are looking for? Python can be used on many operating systems and environments. <a href="/downloads/">View the full list of downloads</a>.</p>
    </div>
    
    <div class="download-os-windows" style="display: none;">
        
        <h4>Download for Windows</h4>
        

        
        <p>
            <a class="button" href="https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe">Python 3.14.0</a>
        </p>
        <p><strong>Note that Python 3.9+ <em>cannot</em> be used on Windows 7 or earlier.</strong></p>
        
        <p>Not the OS you are looking for? Python can be used on many operating systems and environments. <a href="/downloads/">View the full list of downloads</a>.</p>
    </div>
    
    <div class="download-os-macos" style="">
        
        <h4>Download for macOS</h4>
        

        
        <p>
            <a class="button" href="https://www.python.org/ftp/python/3.14.0/python-3.14.0-macos11.pkg">Python 3.14.0</a>
        </p>
        
        
        <p>Not the OS you are looking for? Python can be used on many operating systems and environments. <a href="/downloads/">View the full list of downloads</a>.</p>
    </div>
    
    <div class="download-unknown" style="display: none;">
        <h4>Download Python for Any OS</h4>
        <p>Python can be used on many operating systems and environments.</p>
        <p>
            <a class="button" href="/downloads/operating-systems/">View the full list of downloads</a>
        </p>
    </div>
</li>
</ul>

        
    </li>
    
    
    
    <li id="documentation" class="tier-1 element-3   with-supernav" aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://python-docs-translations.github.io/dashboard/" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
<li class="tier-2 super-navigation">
                                <h4>Python’s standard documentation: download, browse or watch a tutorial.</h4>
                                <p>Get started below, or visit the <a href="/doc/versions/">Documentation page to browse by version</a>. </p>
                                <br>
                                <p class="download-buttons">
                                    <a class="button" href="https://docs.python.org/3/">Python Docs</a> 
                                </p>
                            </li></ul>

        
    </li>
    
    
    
    <li id="community" class="tier-1 element-4   with-supernav" aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>
    
        <li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>
    
                            <li class="tier-2 super-navigation">
                                <h4>The Python Community</h4>
<p>Great software is supported by great people. Our user base is enthusiastic, dedicated to encouraging use of the language, and committed to being diverse and friendly.</p>

<!--
                                <p>Here are some events and groups in your area.</p>
                                <ul class="menu">
                                    <li><time datetime="">9/30<span class="say-no-more">/2012</span></time> <a href="#">Royal Python Society Meetup, Providence RI</a></li>
                                    <li><time datetime="">10/4<span class="say-no-more">/2012</span></time> <a href="#">Python Users Group, Boston MA</a></li>
                                    <li><time datetime="">10/5<span class="say-no-more">/2012</span></time> <a href="#">Python Enthusiasts, Cambridge MA</a></li>
                            </ul>
                            </li>--></li></ul>

        
    </li>
    
    
    
    <li id="success-stories" class="tier-1 element-5   with-supernav" aria-haspopup="true">
        <a href="/success-stories/" title="success-stories" class="">Success Stories</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
    
<!-- successstories supernav from templates/successstories/supernav.html -->
       <li class="tier-2 super-navigation">
            
            <blockquote class="success-quote">
                Want to know how Python is performing on Arm across Linux, Windows, and the cloud? Our 2025 update highlights the latest JIT improvements, ecosystem milestones like GitHub runners and PyTorch on Windows, and the continued collaboration driving it all forward.
            </blockquote>
            <p class="quote-by"><cite>Diego Russo</cite>, <a href="https://www.arm.com">Arm Ltd</a></p>

        </li></ul>

        
    </li>
    
    
    
    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="events" class="tier-1 element-7   with-supernav" aria-haspopup="true">
        <a href="/events/" title="" class=" selected">Events</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
<li class="tier-2 super-navigation">Find events from the Python Community around the world!</li></ul>

        
    </li>
    
    
    
    
  
</ul>

                    
                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->
                    
    

                </div>

                
                

             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content with-right-sidebar" role="main">

                    
                    

                    

                    

    
        <header class="article-header">
            <h3>from the Python Events Calendar</h3>
        </header>
    

    <div class="most-recent-events">
        

        <div class="shrubbery">
            <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
            
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
            
            <ul class="list-recent-events menu">
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/2016/">PyTorch Conference 2025</a>
                        </h3>
                        <p>
                            
                                
                                    
                                        
    <time datetime="2025-10-22T00:00:00+00:00">22 Oct.
        <span id="start-2016" class="say-no-more">
            2025
        </span>

         –
            23 Oct.
        

        <span id="end-2016" class="say-no-more">
            2025
        </span>
    </time>

                                    
                                
                            

                            
                                <span class="event-location">San Francisco, USA
                                    </span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/2105/">PyCon Davao 2025</a>
                        </h3>
                        <p>
                            
                                
                                    
                                        
    <time datetime="2025-10-25T00:00:00+00:00">25 Oct.
        <span id="start-2105" class="say-no-more">
            2025
        </span>

         –
            26 Oct.
        

        <span id="end-2105" class="say-no-more">
            2025
        </span>
    </time>

                                    
                                
                            

                            
                                <span class="event-location">Davao City, Philippines
                                    </span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/1896/">PyCon Sweden</a>
                        </h3>
                        <p>
                            
                                
                                    
                                        
    <time datetime="2025-10-30T00:00:00+00:00">30 Oct.
        <span id="start-1896" class="say-no-more">
            2025
        </span>

         –
            31 Oct.
        

        <span id="end-1896" class="say-no-more">
            2025
        </span>
    </time>

                                    
                                
                            

                            
                                <span class="event-location">Clarion Hotel Skanstull, Stockholm, Sweden
                                    </span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/1999/">PyCon FR 2025</a>
                        </h3>
                        <p>
                            
                                
                                    
                                        
    <time datetime="2025-10-30T00:00:00+00:00">30 Oct.
        <span id="start-1999" class="say-no-more">
            2025
        </span>

         –
            02 Nov.
        

        <span id="end-1999" class="say-no-more">
            2025
        </span>
    </time>

                                    
                                
                            

                            
                                <span class="event-location">Lyon, France
                                    </span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/2111/">PyDay 🎃 + Django Birthday 🦄</a>
                        </h3>
                        <p>
                            
                                
                                    
                                        
    <time datetime="2025-10-31T00:00:00+00:00">31 Oct.
        <span id="start-2111" class="say-no-more">
            2025
        </span>

        <span id="start-2111" class="say-no-more">
            2025
        </span>

        
    </time>

                                    
                                
                            

                            
                                <span class="event-location">Bogotá, Colombia
                                    </span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/2015/">JupyterCon 2025</a>
                        </h3>
                        <p>
                            
                                
                                    
                                        
    <time datetime="2025-11-03T00:00:00+00:00">03 Nov.
        <span id="start-2015" class="say-no-more">
            2025
        </span>

         –
            05 Nov.
        

        <span id="end-2015" class="say-no-more">
            2025
        </span>
    </time>

                                    
                                
                            

                            
                                <span class="event-location">San Diego, USA
                                    </span>
                            
                        </p>
                    </li>
                
            </ul>
        </div>

        
    </div>


                </section>

                
                

                
    <aside class="right-sidebar" role="secondary">
        <div class="sidebar-widget subscribe-widget">
            
            <h2 class="widget-title">Python Event Subscriptions</h2>
            <p>Subscribe to Python Event Calendars:</p>
            <ul class="menu">
                
                
                <li><a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"><span aria-hidden="true" class="icon-ical"></span>Events in iCal format</a></li>
                
            </ul>
            
            <h2 class="widget-title">Python Events Calendars</h2>

<br>

<p>For Python events near you, please have a look at the <a href="http://lmorillas.github.io/python_events/"><b>Python events map</b></a>.</p>

<p>The Python events calendars are maintained by the <a href="https://wiki.python.org/moin/PythonEventsCalendar#Python_Calendar_Team">events calendar team</a>.</p>

<p>Please see the <a href="https://wiki.python.org/moin/PythonEventsCalendar">events calendar project page</a> for details on how to <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event">submit events</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Available_Calendars">subscribe to the calendars</a>, get <a href="https://twitter.com/PythonEvents">Twitter feeds</a> or embed them.</p>

<p>Thank you.</p>

	    </div>

        

        

    </aside>



            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">

                    
                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>

                    

<ul class="sitemap navigation menu do-not-print" role="tree" id="container" style="position: relative; height: 586.344px;">
    
    <li class="tier-1 element-1" style="position: absolute; left: 0px; top: 0px;">
        <a href="/about/">About</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-2" style="position: absolute; left: 155px; top: 0px;">
        <a href="/downloads/">Downloads</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/macos/" title="">macOS</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/downloads/android/" title="">Android</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-3" style="position: absolute; left: 310px; top: 0px;">
        <a href="/doc/">Documentation</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://python-docs-translations.github.io/dashboard/" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="https://peps.python.org" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-4" style="position: absolute; left: 465px; top: 0px;">
        <a href="/community/">Community</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/psf/annual-report/2024/" title="">PSF Annual Impact Report</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="/psf/conduct/" title="">Code of Conduct</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-12" role="treeitem"><a href="/psf/get-involved/" title="">Get Involved</a></li>
    
        <li class="tier-2 element-13" role="treeitem"><a href="/psf/community-stories/" title="">Shared Stories</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-5" style="position: absolute; left: 620px; top: 0px;">
        <a href="/success-stories/" title="success-stories">Success Stories</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/success-stories/category/arts/" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/success-stories/category/business/" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/success-stories/category/education/" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/success-stories/category/engineering/" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/success-stories/category/government/" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/success-stories/category/scientific/" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/success-stories/category/software-development/" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-6" style="position: absolute; left: 775px; top: 0px;">
        <a href="/blogs/" title="News from around the Python world">News</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/psf/newsletter/" title="Python Software Foundation Newsletter">PSF Newsletter</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon US News</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">News from the Community</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-7" style="position: absolute; left: 0px; top: 251px;">
        <a href="/events/">Events</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events/" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-8" style="position: absolute; left: 775px; top: 273px;">
        <a href="/dev/">Contributing</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer's Guide</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="https://github.com/python/cpython/issues" title="">Issue Tracker</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/dev/security/" title="">Report a Security Issue</a></li>
    
</ul>

        
    </li>
    
</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>
                    

                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">
                    
                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/" title="All Systems Operational">Status <span class="python-status-indicator-none" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright ©2001-2025.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="https://policies.python.org/python.org/Privacy-Notice/">Privacy Notice</a></span>
                            <!--&nbsp;<span class="pre"><a href="/psf/community-infrastructure">Powered by PSF Community Infrastructure</a></span>-->
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>
        

    </div><!-- end #touchnav-wrapper -->

    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-ui-1.12.1.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>
    <script src="/static/js/libs/html-includes.js"></script>

    <script type="text/javascript" src="/static/js/main-min.ef82c06437cf.js" charset="utf-8"></script>
    

    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.8af6e26c7a3b.js" charset="utf-8"></script>
    
    
    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.d41d8cd98f00.js" charset="utf-8"></script>
    
    
    <![endif]-->

    

    
    



<script src="chrome-extension://onepmapfbjohnegdmfhndpefjkppbjkm/sm.bundle.js" data-pname="supercopy-v3" data-asset-path="https://spc4.s3.ap-east-1.amazonaws.com"></script></body></html>''')
