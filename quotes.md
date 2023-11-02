---
comments: false
layout: default
title: Quotes
permalink: /quotes
---

<!-- HTML table fragment for page -->
<table>
  <thead>
    <tr>
      <th>Quote</th>
      <th>Upvotes</th>
      <th>Downvotes</th>
    </tr>
  </thead>
  <tbody id="result">
    <!-- javascript generated data -->
  </tbody>
</table>

<!-- Script is laid out in a sequence (without a function) and will execute when the page is loaded -->
<script>

  // prepare HTML-defined "result" container for new output
  const resultContainer = document.getElementById("result");

  // prepare fetch URLs
  const url = "http://allinonebackend.stu.nighthawkcodingsociety.com/api/quotes";  // Use a relative URL to match your Flask API route

  // prepare fetch GET options
  const options = {
    method: 'GET',
    mode: 'cors',
    cache: 'default',
    credentials: 'omit',
    headers: {
      'Content-Type': 'application/json'
    },
  };

  // prepare fetch PUT options, clones with JS Spread Operator (...)
  const put_options = { ...options, method: 'PUT' };

  // fetch the API
  fetch(url, options)
    .then(response => {
      if (response.status !== 200) {
        error('GET API response failure: ' + response.status);
        return;
      }
      response.json().then(data => {
        console.log(data);
        for (const quote of data) {
          const tr = document.createElement("tr");
          
          // td for quote cell
          const quoteCell = document.createElement("td");
          quoteCell.innerHTML = quote.text;

          // td for upvotes
          const upvotesCell = document.createElement("td");
          upvotesCell.innerHTML = quote.upvotes;

          // td for downvotes
          const downvotesCell = document.createElement("td");
          downvotesCell.innerHTML = quote.downvotes;

          // this builds ALL td's (cells) into tr (row) element
          tr.appendChild(quoteCell);
          tr.appendChild(upvotesCell);
          tr.appendChild(downvotesCell);

          // this adds all the tr (row) work above to the HTML "result" container
          resultContainer.appendChild(tr);
        }
      })
    })
    .catch(err => {
      error(err + " " + url);
    });

  // Something went wrong with actions or responses
  function error(err) {
    // log as Error in console
    console.error(err);
    // append error to resultContainer
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.innerHTML = err;
    tr.appendChild(td);
    resultContainer.appendChild(tr);
  }

</script>