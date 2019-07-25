#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
print('''<!DOCTYPE html>
<html>
  <head>
    <title>NaYoung-Welcome</title>
    <meta charset="euc-kr" />
  </head>
  <body>
    <h1><a href="index.html">WEB</a></h1>
    <ol>
      <li><a href="1.html">HTML</a></li>
      <li><a href="2.html">CSS</a></li>
      <li><a href="3.html">JavaScript</a></li>
    </ol>
    <h2>나옹월드</h2>
    <p>
      Welcome~ My name is NaYoung! This is
      <a href="https://www.naver.com/">naver</a>.
    </p>
    <p>
      This is my love song~ <br />
      <iframe
        width="560"
        height="315"
        src="https://youtu.be/52nfjRzIaj8"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </p>
    <!--<img src="cookie.jpg" width="100%">-->
    <img src="cookie.jpg" width="200" />
    <p style="margin-top:40px;">
      <strong>Happy <u>NaYoung</u> world</strong>
    </p>
    <p>
        <div id="disqus_thread"></div>
        <script>
        
        /**
        *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
        *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
        /*
        var disqus_config = function () {
        this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
        this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
        };
        */
        (function() { // DON'T EDIT BELOW THIS LINE
        var d = document, s = d.createElement('script');
        s.src = 'https://web1-tspvdzouqf.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
        })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    </p>
  </body>
</html>
''')
