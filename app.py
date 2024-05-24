<a href="#" id="link-checker">Check Link Safety</a>

<div id="result"></div>

<script>
  const linkInput = document.getElementById('link-input');
  const linkChecker = document.getElementById('link-checker');
  const resultDiv = document.getElementById('result');

  linkChecker.addEventListener('click', () => {
    const linkUrl = linkInput.value.trim();
    if (linkUrl) {
      checkLinkSafety(linkUrl);
    }
  });

  function checkLinkSafety(url) {
    const xhr = new XMLHttpRequest();
    xhr.open('HEAD', url, true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        const headers = xhr.getAllResponseHeaders();
        const referrerPolicy = headers['Referrer-Policy'];
        const contentType = headers['Content-Type'];

        if (referrerPolicy && referrerPolicy.includes('no-referrer')) {
          resultDiv.innerHTML = 'Link is safe: Referrer-Policy is set to no-referrer';
        } else if (contentType && contentType.includes('text/html')) {
          resultDiv.innerHTML = 'Link is safe: Content-Type is set to text/html';
        } else {
          resultDiv.innerHTML = 'Link is not safe: Referrer-Policy or Content-Type is not set correctly';
        }
      } else {
        resultDiv.innerHTML = 'Error: Unable to check link safety';
      }
    };
    xhr.send();
  }
</script>
